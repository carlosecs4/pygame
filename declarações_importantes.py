from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
IMAGENS_DIR = path.join(path.dirname(__file__), 'imagens')
MUSICAS_DIR = path.join(path.dirname(__file__), 'musicas')

# Imagens usadas
fundo_jogo = pygame.image.load("imagens/Cenário 1.jpg")

# POLONI

Poloni_dir = path.join(path.dirname(__file__), 'imagens', 'Poloni sprites') # Guardando endereço das imagens

def define_animação(endereço, posição, n):
    lista = []
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
        lista.append(temp_img)
    return lista

# Alguns arquivos estão invertidos, essa função é igual a anterior, mas também inverte a imagem
def define_animação_virada(endereço, posição, n):
    lista = []
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
        temp_img = pygame.transform.flip(temp_img, True, False)
        lista.append(temp_img)
    return lista

# Animações do Poloni
poloni_parado = define_animação(Poloni_dir, 'Parado', 6)
poloni_andando = define_animação(Poloni_dir, 'Andando', 11)
poloni_socando = define_animação(Poloni_dir, 'Soco', 4)
poloni_agachando = define_animação(Poloni_dir, 'Agachando', 3)
poloni_atacado = define_animação(Poloni_dir, 'Sendo atacado', 5)
poloni_vencendo = define_animação(Poloni_dir, 'Vencendo', 4)
poloni_morto = define_animação(Poloni_dir, 'Morto', 9)
poloni_pulando = define_animação(Poloni_dir, 'Pulando', 7)

imagens_poloni = {
    'PARADO': poloni_parado,
    'ANDANDO': poloni_andando,
    'SOCANDO': poloni_socando,
    'AGACHANDO': poloni_agachando,
    'ATACADO': poloni_atacado,
    'VENCENDO': poloni_vencendo,
    'MORTO': poloni_morto,
    'PULANDO': poloni_pulando
}

# BOB

Bob_dir = path.join(path.dirname(__file__), 'imagens', 'Bob sprites')

# Animações do Bob
bob_parado = define_animação_virada(Bob_dir, 'Parado', 4)
bob_andando = define_animação_virada(Bob_dir, 'Andando', 11)
bob_socando = define_animação_virada(Bob_dir, 'Atacando', 6)
bob_agachando = define_animação_virada(Bob_dir, 'Agachando', 2)
bob_atacado = define_animação_virada(Bob_dir, 'Sendo atacado', 7)

imagens_bob = {
    'PARADO': bob_parado,
    'ANDANDO': bob_andando,
    'SOCANDO': bob_socando,
    'AGACHANDO': bob_agachando,
    'ATACADO': bob_atacado
    }

# DANI
Dani_dir = path.join(path.dirname(__file__), 'imagens', 'Dani sprites')

# Animações da Dani
dani_parado = define_animação_virada(Dani_dir, 'Parado', 11)
dani_andando = define_animação_virada(Dani_dir, 'Andando', 11)
dani_socando = define_animação_virada(Dani_dir, 'Atacando', 9)
dani_agachando = define_animação_virada(Dani_dir, 'Agachando', 3)
dani_atacado = define_animação_virada(Dani_dir, 'Sendo atacado', 5)
dani_vencendo = define_animação_virada(Dani_dir, 'Vencendo', 14)
dani_pulando = define_animação_virada(Dani_dir, 'Pulando', 5)
dani_morto = define_animação_virada(Dani_dir, 'Morto', 8)

imagens_dani = {
    'PARADO': dani_parado,
    'ANDANDO': dani_andando,
    'SOCANDO': dani_socando,
    'AGACHANDO': dani_agachando,
    'ATACADO': dani_atacado,
    'VENCENDO': dani_vencendo,
    'PULANDO': dani_pulando,
    'MORTO': dani_morto
    }

# Julien
Julien_dir = path.join(path.dirname(__file__), 'imagens', 'Julien sprites')

# Animações do Julien
julien_parado = define_animação_virada(Julien_dir, 'Parado', 6)
julien_andando = define_animação_virada(Julien_dir, 'Andando', 12)
julien_socando = define_animação_virada(Julien_dir, 'Atacando', 14)
julien_agachando = define_animação_virada(Julien_dir, 'Agachando', 3)
julien_atacado = define_animação_virada(Julien_dir, 'Sendo atacado', 4)
julien_pulando = define_animação_virada(Julien_dir, 'Pulando', 4)

imagens_julien = {
    'PARADO': julien_parado,
    'ANDANDO': julien_andando,
    'SOCANDO': julien_socando,
    'AGACHANDO': julien_agachando,
    'ATACADO': julien_atacado,
    'PULANDO': julien_pulando
    }

# MÁRCIO

Marcio_dir = path.join(path.dirname(__file__), 'imagens', 'Marcio sprites')

# Animações do Márcio
marcio_parado = define_animação_virada(Marcio_dir, 'Parado', 7)
marcio_andando = define_animação_virada(Marcio_dir, 'Andando', 9)
marcio_socando = define_animação_virada(Marcio_dir, 'Atacando', 14)
marcio_agachando = define_animação_virada(Marcio_dir, 'Agachando', 3)
marcio_atacado = define_animação_virada(Marcio_dir, 'Sendo atacado', 5)
marcio_pulando = define_animação_virada(Marcio_dir, 'Pulando', 6)
marcio_morto = define_animação_virada(Marcio_dir, 'Morto', 6)
marcio_vencendo = define_animação_virada(Marcio_dir, 'Vencendo', 12)

imagens_marcio = {
    'PARADO': marcio_parado,
    'ANDANDO': marcio_andando,
    'SOCANDO': marcio_socando,
    'AGACHANDO': marcio_agachando,
    'ATACADO': marcio_atacado,
    'PULANDO': marcio_pulando,
    'MORTO': marcio_morto,
    'VENCENDO': marcio_vencendo
    }

#  Criando um dicionario que mapeia o nome do personagem ao seu dicionário de imagens
imagens_personagens = {
    'poloni': imagens_poloni,
    'bob': imagens_bob,
    'dani': imagens_dani,
    'julien': imagens_julien,
    'marcio': imagens_marcio
}

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
SELECT = 1
GAME = 2
GAME_OVER = 3
QUIT = 4

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
PARADO = 0
ANDANDO = 1
SOCANDO = 2
AGACHANDO = 3 