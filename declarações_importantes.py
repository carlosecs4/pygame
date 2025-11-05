from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
IMAGENS_DIR = path.join(path.dirname(__file__), 'imagens')
MUSICAS_DIR = path.join(path.dirname(__file__), 'musicas')

# Imagens usadas
fundo_jogo = pygame.image.load("imagens/cenário 2.png")
bob = pygame.image.load("imagens/Bob.png")
gabriel = pygame.image.load("imagens/Gabriel.png")

# Tamnho dos personagens
player_width = 60
player_height = 160

# Dados gerais do jogo.
TITULO = 'INSPER FIGHT'
LARGURA = 1100# Largura da tela
ALTURA = 650 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define a velocidade inicial no pulo
VELOCIDADE_PULO = 500  # px / s
# Define a altura do chão
CHAO = ALTURA * 5 // 6

# Estados possíveis do jogo
INIT = 0
GAME = 1
QUIT = 2

#connstantes que estavam em jump_plataform:
# Dados gerais do jogo.
WIDTH = 1280 # Largura da tela
HEIGHT = 720 # Altura da tela
TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
PLAYER_WIDTH = TILE_SIZE
PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 8
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5


# Define os tipos de tiles
BLOCK = 0
PLATF = 1
EMPTY = -1

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2