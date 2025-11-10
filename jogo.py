import pygame
from declarações_importantes import *
from tela_do_jogo import *
from tela_de_inicio import *
from tela_de_selecao import *
from game_over import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Criando a tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

#Loop principal do jogo
estado = INIT
while estado != QUIT:
    if estado == INIT:
        estado = tela_inicio(tela)   # tela_inicio faz seu loop e retorna o estado
    elif estado == SELECT:
        selecoes = tela_selecao(tela)
        estado = selecoes[0] # tela_selecao faz seu loop e retorna o estado no primeiro indice
        personagem1 = selecoes[1]  # tela_selecao retorna o personagem 1 no segundo indice
        personagem2 = selecoes[2]  # tela_selecao retorna o personagem 2 no terceiro indice
    elif estado == GAME:
        #game screen retorna uma lista com o estado e também o jogador vencedor.
        seleções = game_screen(tela, personagem1, personagem2)   # agora game_screen retorna o próximo estado
        estado = seleções[0]
        ganhador = seleções[1]
    elif estado == GAME_OVER:
        estado = game_over(tela, ganhador, estado)
        print(estado)
    else:
        estado = QUIT

pygame.quit()