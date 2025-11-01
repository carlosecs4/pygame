from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
IMAGENS_DIR = path.join(path.dirname(__file__), 'imagens')
MUSICAS_DIR = path.join(path.dirname(__file__), 'musicas')

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

# Define a aceleração da gravidade
GRAVIDADE = 1000  # px / s^2
# Define a velocidade inicial no pulo
VELOCIDADE_PULO = 500  # px / s
# Define a altura do chão
CHAO = ALTURA * 5 // 6

# Define estados possíveis do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2

# Estados possíveis do jogo
INIT = 0
GAME = 1
QUIT = 2