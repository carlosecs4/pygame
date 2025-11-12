from os import path
import os
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
IMAGENS_DIR = path.join(path.dirname(__file__), 'imagens')
MUSICAS_DIR = path.join(path.dirname(__file__), 'musicas')

# Imagens usadas
fundo_jogo = pygame.image.load(path.join(IMAGENS_DIR, "Cenário 1.jpg"))
posições = ['Parado', 'Andando', 'Atacando', 'Agachando', 'Sendo atacado','Vencendo', 'Morto', 'Pulando', 'Defendendo', "Especial"]
nomes = ['Poloni', 'Bob', 'Dani', 'Julien', 'Marcio', 'Gabriel']

def define_animação(nome, posição, tamanho=160):
    lista = []
    endereço = path.join(path.dirname(__file__), 'imagens', f'{nome} sprites', posição)
    n = len(os.listdir(endereço))
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * tamanho / temp_img.get_height(), tamanho))
        if nome != 'Poloni':
            temp_img = pygame.transform.flip(temp_img, True, False)
        lista.append(temp_img)
    return lista

# POLONI
imagens_personagens = {}
for i in range(len(nomes)):
    animação = {}
    for posição in posições:
        if posição != 'Especial':
            animação[posição.upper()] = define_animação(nomes[i], posição)
        else:
            especial = pygame.image.load(path.join(path.dirname(__file__), 'imagens', f'{nomes[i]} sprites', 'Especial', '1.png'))
            animação[posição.upper()] = pygame.transform.scale(especial, (80, 80))
    imagens_personagens[nomes[i].lower()] = animação

# Dados gerais do jogo.
TITULO = 'INSPER FIGHT'
LARGURA = 1000 # Largura da tela
ALTURA = 550 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Estados possíveis do jogo
INIT = 0
SELECT = 1
GAME = 2
GAME_OVER = 3
QUIT = 4

# Dados gerais da imagem de fundo original
WIDTH = 1280 # Largura 
HEIGHT = 720 # Altura

FPS = 60 # Frames por segundo

# Define a aceleração da gravidade
GRAVITY = 5