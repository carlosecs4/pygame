import pygame
import random
from os import path
from declarações_importantes import *

pygame.font.init()

font_ganhador = pygame.font.Font("fontes/mk2.ttf", 60)
font_aviso = pygame.font.Font("fontes/mk5style.ttf", 30)

def game_over(tela, ganhador, estado):
    #aqui, usei IA para saber qual fonte seria melhor usar, como poderia ajudar usar a fonte de uma melhor forma, e também para corrigir os bugs.
    clock = pygame.time.Clock()

    tela.fill(BLACK)
    
    #cria um texto que diz qual é o ganhador.
    texto = font_ganhador.render(f'PLAYER {ganhador} WINS', True, VERDE)
    texto2 = font_aviso.render('pressione ENTER para recomeçar', True, VERMELHO)

    text_rect = texto.get_rect(center=(LARGURA/2, ALTURA/2))
    text_rect2 = texto2.get_rect(center=(LARGURA / 2, ALTURA * (3 / 4)))
    tela.blit(texto, text_rect)
    tela.blit(texto2, text_rect2)
    pygame.display.flip()

    while estado == GAME_OVER:

        clock.tick(FPS)
        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                estado = QUIT

            #verifica se apertou enter
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    estado = SELECT
        
        tela.fill(PRETO)

        tela.blit(texto, text_rect)
        tela.blit(texto2, text_rect2)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado
