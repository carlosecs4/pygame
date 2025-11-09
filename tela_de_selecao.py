# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from declarações_importantes import *

# Função para a tela de seleção de personagem
def tela_selecao(tela):
    clock = pygame.time.Clock()
    selecionado = 0
    personagens = ['poloni', 'bob', 'dani', 'julien']
    font = pygame.font.SysFont(None, 30)

    # Lista com as imagens dos personagens, feita com ajuda do copilot
    imagens_personagens = [pygame.image.load(path.join(IMAGENS_DIR, f'{p} sprites\Foto para seleção\{p} perfil.jpg')) for p in personagens]

    # Loop de seleção para o player 1
    selecionando = True
    while selecionando:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if selecionado - 1 < 0:
                        selecionado = len(imagens_personagens) - 1
                    else:
                        selecionado = (selecionado - 1)
                elif event.key == pygame.K_RIGHT:
                    if selecionado + 1 >= len(imagens_personagens):
                        selecionado = 0
                    else:
                        selecionado = (selecionado + 1)
                elif event.key == pygame.K_RETURN:
                    selecionando = False
                    estado = GAME  # Prosseguir para o jogo após seleção
                    personagem1 = personagens[selecionado]
        
        tela.fill(PRETO)
        texto = font.render("Player 1 selecione seu personagem", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 50))
        
        personagem_atual = imagens_personagens[selecionado]
        tela.blit(personagem_atual, (LARGURA // 2 - personagem_atual.get_width() // 2, ALTURA // 2 - personagem_atual.get_height() // 2))
        
        instrucoes = font.render("Use as setas para selecionar e Enter para confirmar", True, BRANCO)
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - 100))
        
        pygame.display.flip()
    
    # Loop de seleção para o player 2
    selecionado = 0
    selecionando = True
    while selecionando:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selecionado = (selecionado - 1) % len(imagens_personagens)
                elif event.key == pygame.K_RIGHT:
                    selecionado = (selecionado + 1) % len(imagens_personagens)
                elif event.key == pygame.K_RETURN:
                    personagem2 = personagens[selecionado]
                    if personagem2 == personagem1:
                        # Evitar que o player 2 escolha o mesmo personagem do player 1
                        aviso = font.render("Personagem já selecionado! Escolha outro.", True, VERMELHO)
                        tela.blit(aviso, (LARGURA // 2 - aviso.get_width() // 2, ALTURA - 150))
                        pygame.display.flip()
                        pygame.time.delay(1500) # Espera o player ler o aviso
                        continue
                    selecionando = False
                    estado = GAME  # Prosseguir para o jogo após seleção
        
        tela.fill(PRETO)
        texto = font.render("Player 2 selecione seu personagem", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 50))
        
        personagem_atual = imagens_personagens[selecionado]
        tela.blit(personagem_atual, (LARGURA // 2 - personagem_atual.get_width() // 2, ALTURA // 2 - personagem_atual.get_height() // 2))
        
        instrucoes = font.render("Use as setas para selecionar e Enter para confirmar", True, BRANCO)
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - 100))
        
        pygame.display.flip()
    
    return [estado, personagem1, personagem2]