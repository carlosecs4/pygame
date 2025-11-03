import pygame
from declarações_importantes import *
from jump_platform import *
from tela_de_inicio import *

pygame.init()
pygame.mixer.init()

# Criando a tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

#Loop principal do jogo
estado = INIT
while estado != QUIT:
    if estado == INIT:
        estado = tela_inicio(tela)   # tela_inicio faz seu loop e retorna o estado
    elif estado == GAME:
        estado = game_screen(tela)   # agora game_screen retorna o próximo estado
    else:
        estado = QUIT
 

pygame.quit()
