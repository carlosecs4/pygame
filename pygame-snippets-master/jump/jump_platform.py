# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from declarações_importantes import *

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.attack_type = 0

    def move(self, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        self.vel_y = 0

        #teclas precionadas
        key = pygame.key.get_pressed()

        if self.attacking == False:
            if self.attacking == False:
                #movimentos
                if key[pygame.K_a]:
                    dx = -SPEED
                
                if key[pygame.K_d]:
                    dx = SPEED

                #pular
                if key[pygame.K_w] and not self.jump:
                    self.vel_y = -30
                    self.jump = True 

                #attack
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(surface, target)
                    #determinando qual tipo de ataque será usado
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2


        #aplicando a gravidade:
        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right
        if self.rect.bottom + dy > HEIGHT - 230:
            self.vel_y = 0
            self.jump = False
            dy = HEIGHT - 230 - self.rect.bottom

        #atualiza a posição do jogador:
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        hits = attacking_rect.colliderect(target)
        self.attacking = True
        if hits:
            print("Hit")
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

fundo_jogo = pygame.image.load("pygame-snippets-master/jump/imagens/cenário 2.png")

def desenha_fundo():
    fundo_escalado = pygame.transform.scale(fundo_jogo, (WIDTH, HEIGHT))
    tela.blit(fundo_escalado, (0,0))

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    desenha_fundo()

    # Cria o sprite de 2 jogadores:
    player1 = Player(200, 310)
    player2 = Player(700, 310)

    state = GAME

    while state != QUIT:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        desenha_fundo()

        # Variável para poder atualizar todos os sprites de uma vez

        player1.move(tela, player2)

        player1.draw(tela)
        player2.draw(tela)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d:
                    player1.move(tela, player2)
                if event.key == pygame.K_r or event.key == pygame.K_t:
                    player1.attack(tela, player2)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r or event.key == pygame.K_t:
                    player1.attacking = False
        
        player1.update()

        pygame.display.update()