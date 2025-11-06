# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from declarações_importantes import *

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Classe do Player 1
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.attack_type = 0
        self.health = 100
        self.virar = False
        
        # Variáveis de animação
        self.animacoes = assets
        self.movimento_atual = 'PARADO'
        self.frame = 0
        self.imagem = assets[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
        self.ultimo_update = pygame.time.get_ticks()

        self.frame_ticks = 120  # Tempo entre frames

    def move(self, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        self.vel_y = 0
        
        # Essas duas precisam ser falsas para atualizar a animação se o jogador soltar as teclas de movimento ou ataque
        self.correndo = False
        self.attacking = False 

        #teclas precionadas
        key = pygame.key.get_pressed()

        if self.attacking == False:
            if self.attacking == False:
                #movimentos
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.correndo = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.correndo = True

                #pular
                if key[pygame.K_w] and not self.jump:
                    self.vel_y = -100
                    self.jump = True 

                #attack
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(surface, target)
                    self.attacking = True
                    #determinando qual tipo de ataque será usado
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
        
        #Garantir que os jogadores estão virados um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.virar = False
        else:
            self.virar = True

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
        # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
        if self.virar == False:
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        else:
            attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
        hits = attacking_rect.colliderect(target)
        self.attacking = True
        if hits:
            target.health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    # Método para desenhar o jogador
    def draw(self, surface):
        imagem_ajustada = pygame.transform.flip(self.imagem, self.virar, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(imagem_ajustada, (self.rect.x, self.rect.y))
    
    # Método para atualizar a animação do jogador
    def update(self):
        # Checa o estado atual para definir a animação correta
        if self.attacking:
            # Se o movimento novo não for o mesmo que o anterior, reinicia a animação
            if self.movimento_atual != 'SOCANDO':
                self.movimento_atual = 'SOCANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.correndo:
            if self.movimento_atual != 'ANDANDO':
                self.movimento_atual = 'ANDANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        
        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        if tempo > self.frame_ticks:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= len(self.animacoes[self.movimento_atual]):
                self.frame = 0

# Classe para o player 2 (mesma coisa que o P1, mas com teclas de movimento e ataque diferentes)
class Player2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.attack_type = 0
        self.health = 100
        self.virar = False
        
        # Variáveis de animação
        self.animacoes = assets
        self.movimento_atual = 'PARADO'
        self.frame = 0
        self.imagem = assets[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
        self.ultimo_update = pygame.time.get_ticks()

        self.frame_ticks = 120  # Tempo entre frames

    def move(self, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        self.vel_y = 0
        
        # Essas duas precisam ser falsas para atualizar a animação se o jogador soltar as teclas de movimento ou ataque
        self.correndo = False
        self.attacking = False 

        #teclas precionadas
        key = pygame.key.get_pressed()

        if self.attacking == False:
            if self.attacking == False:
                #movimentos
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.correndo = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.correndo = True

                #pular
                if key[pygame.K_UP] and not self.jump:
                    self.vel_y = -100
                    self.jump = True 

                #attack
                if key[pygame.K_RSHIFT] or key[pygame.K_KP0]:
                    self.attack(surface, target)
                    self.attacking = True
                    #determinando qual tipo de ataque será usado
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
        
        #Garantir que os jogadores estão virados um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.virar = False
        else:
            self.virar = True

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
        # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
        if self.virar == False:
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        else:
            attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
        hits = attacking_rect.colliderect(target)
        self.attacking = True
        if hits:
            target.health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    # Método para desenhar o jogador
    def draw(self, surface):
        imagem_ajustada = pygame.transform.flip(self.imagem, self.virar, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(imagem_ajustada, (self.rect.x, self.rect.y))
    
    # Método para atualizar a animação do jogador
    def update(self):
        # Checa o estado atual para definir a animação correta
        if self.attacking:
            # Se o movimento novo não for o mesmo que o anterior, reinicia a animação
            if self.movimento_atual != 'SOCANDO':
                self.movimento_atual = 'SOCANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.correndo:
            if self.movimento_atual != 'ANDANDO':
                self.movimento_atual = 'ANDANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        
        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        if tempo > self.frame_ticks:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= len(self.animacoes[self.movimento_atual]):
                self.frame = 0
        
def desenha_fundo():
    fundo_escalado = pygame.transform.scale(fundo_jogo, (WIDTH, HEIGHT))
    tela.blit(fundo_escalado, (0,0))

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

# função para criar a barra de vida
def desenha_barra_de_vida(health,x,y):
    ratio = health / 100
    pygame.draw.rect(tela,AMARELO, (x,y,400, 30))
    pygame.draw.rect(tela,VERMELHO, (x, y ,400 * ratio ,30))

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    desenha_fundo()
    # Cria o sprite de 2 jogadores:
    player1 = Player(200, 400, imagens_poloni)
    player2 = Player2(700, 310, imagens_poloni)

    state = GAME

    while state != QUIT:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        desenha_fundo()

         # mostra a barra de vida
        desenha_barra_de_vida(player1.health, 20, 20)
        desenha_barra_de_vida(player2.health,680,20)

        # Variável para poder atualizar todos os sprites de uma vez

        player1.move(tela, player2)
        player2.move(tela, player1)

        player1.draw(tela)
        player2.draw(tela)

        # Atualiza a animação dos jogadores
        player1.update()
        player2.update()

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_a or event.key == pygame.K_d:
                    player1.move(tela, player2)
                if event.key == pygame.K_r or event.key == pygame.K_t:
                    player1.attack(tela, player2)
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player2.move(tela, player1)
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_KP0:
                    player2.attack(tela, player1)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r or event.key == pygame.K_t:
                    player1.attacking = False
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_KP0:
                    player2.attacking = False

        pygame.display.update()
