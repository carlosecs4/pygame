import pygame
import random
from os import path
from declarações_importantes import *

# Função para a tela de seleção de personagem
def tela_selecao(tela):
    clock = pygame.time.Clock()
    # Variável para armazenar o personagem selecionado
    selecionado = 0

    # Lista de personagens disponíveis
    font = pygame.font.Font("fontes/mk5style.ttf", 30)

    # Lista com as imagens dos personagens
    imagens_personagens = []
    for personagem in nomes:
        imagens_personagens.append(pygame.image.load(path.join(IMAGENS_DIR, f'{personagem} sprites\Foto para seleção\{personagem} perfil.jpg')))

     # Carrega e toca música de fundo (COLOCA ISSO NO ASSETS DEPOIS)
    pygame.mixer.music.load(path.join(MUSICAS_DIR, 'Tela de seleção.ogg'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # Loop de seleção para o player 1
    # Algumas parte feitas com ajuda do CoPilot (linhas indicadas por *)
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
                    personagem1 = nomes[selecionado].lower()
        
        tela.fill(PRETO)
        
        personagem_atual = imagens_personagens[selecionado]
        # Redimensionando a foto
        personagem_atual = pygame.transform.scale(personagem_atual, (personagem_atual.get_width() * 400 / personagem_atual.get_height(), 400))

        # Centralizando os textos e imagens (*)
        tela.blit(personagem_atual, (LARGURA // 2 - personagem_atual.get_width() // 2, ALTURA // 2 - personagem_atual.get_height() // 2))

        texto = font.render("Player 1 selecione seu personagem", True, VERMELHO)
        # (*)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 0))
        
        instrucoes = font.render("Use as setas para selecionar e Enter para confirmar", True, VERMELHO)
        # (*)
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - instrucoes.get_height()))
        
        pygame.display.update()
    
    # Loop de seleção para o player 2 (Mesma coisa que o Loop 1, mas com um avio
    # para os players não escolherem os mesmos personagens)
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
                    personagem2 = nomes[selecionado].lower()
                    if personagem2 == personagem1:
                        # Evitar que o player 2 escolha o mesmo personagem do player 1
                        aviso = font.render("Personagem já selecionado! Escolha outro!", True, VERMELHO)
                        tela.blit(aviso, (LARGURA // 2 - aviso.get_width() // 2, ALTURA // 2 - aviso.get_height() // 2)) # Centro da tela
                        pygame.display.update()
                        pygame.time.delay(1000) # Da tempo pro player ler o aviso
                        continue
                    selecionando = False
                    estado = GAME  # Redireciona para a tela do jogo 
        
        tela.fill(PRETO)
        
        personagem_atual = imagens_personagens[selecionado]
        # Redimensionando a foto
        personagem_atual = pygame.transform.scale(personagem_atual, (personagem_atual.get_width() * 400 / personagem_atual.get_height(), 400))

        # Centralizando os textos e imagens (*)
        tela.blit(personagem_atual, (LARGURA // 2 - personagem_atual.get_width() // 2, ALTURA // 2 - personagem_atual.get_height() // 2))

        texto = font.render("Player 2 selecione seu personagem", True, VERMELHO)
        # (*)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 0))
        
        instrucoes = font.render("Use as setas para selecionar e Enter para confirmar", True, VERMELHO)
        # (*)
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - instrucoes.get_height()))
        
        pygame.display.update()
        pygame.display.update()
    pygame.mixer.music.stop()
    return [estado, personagem1, personagem2]