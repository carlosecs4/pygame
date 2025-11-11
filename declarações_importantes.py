from os import path
import os
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
IMAGENS_DIR = path.join(path.dirname(__file__), 'imagens')
MUSICAS_DIR = path.join(path.dirname(__file__), 'musicas')

# Imagens usadas
fundo_jogo = pygame.image.load(path.join(IMAGENS_DIR, "Cenário 1.jpg"))
posições = ['parado', 'andando', 'socando', 'agachando', 'atacado','vencendo', 'morto', 'pulando']
nomes = ['poloni', 'bob', 'dani', 'julien', 'marcio', 'gabriel']

# POLONI

Poloni_dir = path.join(path.dirname(__file__), 'imagens', 'Poloni sprites') # Guardando endereço das imagens

# def define_animação(nome, endereço, posição):
#     lista = []
#     n = len(os.listdir(f'{nome}\{posição}'))
#     for i in range(1, n):
#         temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
#         temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
#         lista.append(temp_img)
#     return lista


def define_animação(nome, endereço, posição):
    lista = []
    n = len(os.listdir(f'{nome}\{posição}'))
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
        lista.append(temp_img)
    return lista

# Alguns arquivos estão invertidos, essa função é igual a anterior, mas também inverte a imagem
# def define_animação_virada(nome, endereço, posição):
#     lista = []
#     n = len(os.listdir(f'{nome}\{posição}'))
#     for i in range(1, n):
#         temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
#         temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
#         temp_img = pygame.transform.flip(temp_img, True, False)
#         lista.append(temp_img)
#     return lista

def define_animação_virada(endereço, posição, n):
    lista = []
    for i in range(1, n):
        temp_img = pygame.image.load(path.join(endereço, f'{posição}\{i}.png'))
        temp_img = pygame.transform.scale(temp_img, (temp_img.get_width() * 160 / temp_img.get_height(), 160))
        temp_img = pygame.transform.flip(temp_img, True, False)
        lista.append(temp_img)
    return lista


# Animações do Poloni
poloni_parado = define_animação(Poloni_dir, 'Parado')
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

#adicionando um loop para o código ser menor:
#aqui, usei IA para saber como faria para acessar a quantidade de imagens na pasta
# imagens_poloni = {}
# for i in range(len(posições)):
#     imagens_poloni[posições[i].upper()] = define_animação('poloni', Poloni_dir, posições[i])

# BOB

Bob_dir = path.join(path.dirname(__file__), 'imagens', 'Bob sprites')

# Animações do Bob
bob_parado = define_animação_virada(Bob_dir, 'Parado', 4)
bob_andando = define_animação_virada(Bob_dir, 'Andando', 11)
bob_socando = define_animação_virada(Bob_dir, 'Atacando', 6)
bob_agachando = define_animação_virada(Bob_dir, 'Agachando', 2)
bob_atacado = define_animação_virada(Bob_dir, 'Sendo atacado', 7)
bob_morto = define_animação_virada(Bob_dir, 'Morto', 5)
bob_vencendo = define_animação_virada(Bob_dir, 'Vencendo', 8)
bob_pulando = define_animação_virada(Bob_dir, "Pulando", 2)

imagens_bob = {
    'PARADO': bob_parado,
    'ANDANDO': bob_andando,
    'SOCANDO': bob_socando,
    'AGACHANDO': bob_agachando,
    'ATACADO': bob_atacado,
    'VENCENDO': bob_vencendo,
    'MORTO': bob_morto,
    'PULANDO': bob_pulando
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
julien_morto = define_animação_virada(Julien_dir, "Morto", 4)
julien_vencendo = define_animação_virada(Julien_dir, "Vencendo", 8)

imagens_julien = {
    'PARADO': julien_parado,
    'ANDANDO': julien_andando,
    'SOCANDO': julien_socando,
    'AGACHANDO': julien_agachando,
    'ATACADO': julien_atacado,
    'PULANDO': julien_pulando,
    'MORTO': julien_morto,
    'VENCENDO': julien_vencendo
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

#GABRIEL
gabriel_dir = path.join(path.dirname(__file__), 'imagens', 'Gabriel sprites')

gabriel_parado = define_animação_virada(gabriel_dir, "Parado")
gabriel_andando = define_animação_virada(gabriel_dir, 'Andando')
gabriel_socando = define_animação_virada(gabriel_dir, 'Atacando')
gabriel_agachando = define_animação_virada(gabriel_dir, 'Agachando')
gabriel_atacado = define_animação_virada(gabriel_dir, 'Sendo atacado')
gabriel_pulando = define_animação_virada(gabriel_dir, 'Pulando')
gabriel_morto = define_animação_virada(gabriel_dir, 'Morto')
gabriel_vencendo = define_animação_virada(gabriel_dir, 'Vencendo')

imagens_gabriel = {
    'PARADO': gabriel_parado,
    'ANDANDO': gabriel_andando,
    'SOCANDO:': gabriel_socando,
    'AGACHANDO': gabriel_agachando,
    'ATACADO': gabriel_atacado,
    'PULANDO': gabriel_pulando,
    'MORTO': gabriel_morto,
    'VENCENDO': gabriel_vencendo
}

#  Criando um dicionario que mapeia o nome do personagem ao seu dicionário de imagens
imagens_personagens = {
    'poloni': imagens_poloni,
    'bob': imagens_bob,
    'dani': imagens_dani,
    'julien': imagens_julien,
    'marcio': imagens_marcio,
    'gabriel': imagens_gabriel
}

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
GRAVITY = 6