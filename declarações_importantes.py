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

def define_animação(nome, endereço, posição, n, m):
    lista = []
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{posição}/{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() / m, temp_img.get_height() / m))
        lista.append(temp_img)
    return lista

# animações_poloni = {}
poloni_parado = []
for i in range(1, 6):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Parado/Poloni parado {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_parado.append(temp_img)

# animações_poloni['parado'] = define_animação("poloni", Poloni_dir, 'Parado', 6, 3)

poloni_andando = []
for i in range(1, 11):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Andando/Poloni andando {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_andando.append(temp_img)

poloni_socando = []
for i in range(1, 4):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Soco/Poloni soco {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_socando.append(temp_img)

poloni_agachando = []
for i in range(1, 3):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Agachando/Poloni agachando {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_agachando.append(temp_img)

poloni_atacado = []
for i in range(1, 5):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Sendo atacado/Poloni atacado {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_atacado.append(temp_img)

poloni_vencendo = []
for i in range(1, 4):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Vencendo/Poloni vencendo {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_vencendo.append(temp_img)

poloni_morto = []
for i in range(1, 9):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Morto/Poloni morto {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_morto.append(temp_img)

poloni_pulando = []
for i in range(1, 7):
    temp_img = pygame.image.load(path.join(Poloni_dir, f'Pulando/Poloni pulando {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    poloni_pulando.append(temp_img)

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

bob_parado = []
for i in range(1, 4):
    temp_img = pygame.image.load(path.join(Bob_dir, f'Parado/Bob parado {i}.png'))
    # Todas as imagens do Bob são redimensionadas e espelhadas (Estão viradas para o lado errado nos arquivos)

    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    bob_parado.append(temp_img)

bob_andando = []
for i in range(1, 11):
    temp_img = pygame.image.load(path.join(Bob_dir, f'Andando/Bob andando {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (temp_img.width, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    bob_andando.append(temp_img)

bob_socando = []
for i in range(1, 6):
    temp_img = pygame.image.load(path.join(Bob_dir, f'Atacando/Bob atacando {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    bob_socando.append(temp_img)

bob_agachando = []
temp_img = pygame.image.load(path.join(Bob_dir, f'Agachando/Bob agachando.png'))
temp_img = pygame.transform.scale(temp_img, (60, 160))
temp_img = pygame.transform.flip(temp_img, True, False)
bob_agachando.append(temp_img)

bob_atacado = []
for i in range(1, 7):
    temp_img = pygame.image.load(path.join(Bob_dir, f'Sendo atacado/Bob atacado {i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    bob_atacado.append(temp_img)

imagens_bob = {
    'PARADO': bob_parado,
    'ANDANDO': bob_andando,
    'SOCANDO': bob_socando,
    'AGACHANDO': bob_agachando,
    'ATACADO': bob_atacado
    }

# DANI
Dani_dir = path.join(path.dirname(__file__), 'imagens', 'Dani sprites')

dani_parado = []
for i in range(1, 11):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Parado\{i}.png'))
    # Todas as imagens da Dani são redimensionadas e espelhadas (Estão viradas para o lado errado nos arquivos)

    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_parado.append(temp_img)

dani_andando = []
for i in range(1, 11):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Andando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_andando.append(temp_img)

dani_socando = []
for i in range(1, 9):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Atacando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_socando.append(temp_img)

dani_agachando = []
for i in range(1, 3):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Agachando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_agachando.append(temp_img)

dani_atacado = []
for i in range(1, 5):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Sendo atacado\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_atacado.append(temp_img)

dani_vencendo = []
for i in range(1, 14):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Vencendo\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_vencendo.append(temp_img)

dani_pulando = []
for i in range(1, 5):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Pulando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_pulando.append(temp_img)

dani_morto = []
for i in range(1, 8):
    temp_img = pygame.image.load(path.join(Dani_dir, f'Morto\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    dani_morto.append(temp_img)

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

julien_parado = []
for i in range(1, 6):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Parado\{i}.png'))
    # Todas as imagens do Julien são redimensionadas e espelhadas (Estão viradas para o lado errado nos arquivos)

    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_parado.append(temp_img)

julien_andando = []
for i in range(1, 12):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Andando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_andando.append(temp_img)

julien_socando = []
for i in range(1, 14):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Atacando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_socando.append(temp_img)

julien_agachando = []
for i in range(1, 3):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Agachando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_agachando.append(temp_img)

julien_atacado = []
for i in range(1, 4):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Sendo atacado\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_atacado.append(temp_img)

julien_pulando = []
for i in range(1, 4):
    temp_img = pygame.image.load(path.join(Julien_dir, f'Pulando\{i}.png'))
    temp_img = pygame.transform.scale(temp_img, (60, 160))
    temp_img = pygame.transform.flip(temp_img, True, False)
    julien_pulando.append(temp_img)

imagens_julien = {
    'PARADO': julien_parado,
    'ANDANDO': julien_andando,
    'SOCANDO': julien_socando,
    'AGACHANDO': julien_agachando,
    'ATACADO': julien_atacado,
    'PULANDO': julien_pulando
    }

#  Criando um dicionario que mapeia o nome do personagem ao seu dicionário de imagens
imagens_personagens = {
    'poloni': imagens_poloni,
    'bob': imagens_bob,
    'dani': imagens_dani,
    'julien': imagens_julien
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