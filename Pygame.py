# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 1280
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Logo do jogo')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
HEIGHT_IMAGE = 512
WIDTH_IMAGE = 512
image = pygame.image.load('imagens/Logo do jogo.png').convert()
image = pygame.transform.scale(image, (WIDTH_IMAGE,HEIGHT_IMAGE))
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (WIDTH / 2 - WIDTH_IMAGE / 2, HEIGHT / 2 - HEIGHT_IMAGE / 2))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados