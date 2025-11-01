import pygame
from constantes import *
from tela_do_jogo import inicializa, game_loop
from tela_de_inicio import *


# Classe Jogador que representa o herói
class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogador_img):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.estado = PARADO

        # Aumenta o tamanho da imagem para ficar mais fácil de ver
        jogador_img = pygame.transform.scale(jogador_img, (100, 160))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = jogador_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no topo da janela e cai até o chão
        self.rect.centerx = LARGURA / 2
        self.rect.top = 0

        self.velocidade_y = 0

    # Metodo que atualiza a posição do personagem
    def update(self, dt):
        self.velocidade_y += GRAVIDADE * dt
        # Atualiza o estado para caindo
        if self.velocidade_y > 0:
            self.estado = CAINDO
        self.rect.y += self.velocidade_y * dt
        # Se bater no chão, para de cair
        if self.rect.bottom >= CHAO:
            # Reposiciona para a posição do chão
            self.rect.bottom = CHAO
            # Para de cair
            self.velocidade_y = 0
            # Atualiza o estado para parado
            self.estado = PARADO

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.estado == PARADO:
            self.velocidade_y -= VELOCIDADE_PULO
            self.estado = PULANDO


pygame.init()
pygame.mixer.init()

# Criando a tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

estado = INIT
while estado != QUIT:
    if estado == INIT:
        estado = tela_inicio(tela)
    elif estado == GAME:
        tela, estado = inicializa()
        game_loop(tela, estado)
    else:
        estado = QUIT