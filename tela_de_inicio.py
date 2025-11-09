import pygame
import random
from declarações_importantes import *

def tela_inicio(tela):
    # Variável para ajustar a velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = pygame.image.load(path.join(IMAGENS_DIR, 'Logo do jogo.png')).convert()
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()
    font = pygame.font.SysFont(None, 30)
    
    # Cria texto para falar pro jogador apertar qualquer tecla para jogar
    texto = font.render('Aperte qualquer tecla para jogar', True, (255, 50, 50))
    
    # Carrega e toca música de fundo
    pygame.mixer.music.load(path.join(MUSICAS_DIR, 'Tela de início.ogg'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    rodando = True
    while rodando:

        clock.tick(FPS)
        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if event.type == pygame.KEYUP:
                estado = SELECT
                pygame.mixer.music.stop()
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(fundo, fundo_rect)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA - 100))
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado