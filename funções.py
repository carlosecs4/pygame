import pygame
from declarações_importantes import *

def inicializa():

    pygame.init()
    pygame.mixer.init()

    # Criando a tela do jogo
    window = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    # Imprime instruções
    print('*' * len(TITULO))
    print(TITULO.upper())
    print('*' * len(TITULO))
    print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

    # Carrega imagem
    jogador_img = pygame.image.load(path.join(IMG_DIR, 'hero-single.png')).convert_alpha()

    # Cria Sprite do jogador
    jogador = Jogador(jogador_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)

    estado = {
        'jogador': jogador,
        'todos_sprites': todos_sprites,
        'clock': pygame.time.Clock(),
    }

    return window, estado


def atualiza_estado(estado):
    dt = estado['clock'].tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera o estado do jogador.
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                estado['jogador'].jump()

    # Depois de processar os eventos.
    # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
    estado['todos_sprites'].update(dt)

    return True


def desenha(window, estado):
    window.fill(PRETO)
    # Desenha chão
    pygame.draw.rect(window, VERDE, (0, CHAO, LARGURA, ALTURA - CHAO))
    estado['todos_sprites'].draw(window)

    pygame.display.update()


def game_loop(window, estado):
    while atualiza_estado(estado):
        desenha(window, estado)