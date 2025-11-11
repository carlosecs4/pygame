# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from declarações_importantes import *
from tela_de_selecao import *

# Classe do Player 1
class Player1(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)

        #variaveis que indicam o movimento
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.attack_type = 0
        self.health = 100
        self.virar = False
        self.agachar = False
        self.defender = False
        self.morto = False
        self.vencendo = False
        
        # Variáveis de animação
        self.animacoes = assets
        self.movimento_atual = 'PARADO'
        self.frame = 0
        self.imagem = assets[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
        self.ultimo_update = pygame.time.get_ticks()

        self.frame_ticks_animacao = 150  # Tempo entre frames
        
        # Só será possível atacar a cada 200 milissegundos
        self.ultimo_ataque = pygame.time.get_ticks()  # Cooldown para o ataque
        self.frame_ticks_ataque = 150 * (len(assets['SOCANDO']) + 1)  # Tempo entre ataques (50 ms para cada frame de animação)

    def move(self, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        self.vel_y = 0

        # Essas duas precisam ser falsas para atualizar a animação se o jogador soltar as teclas de movimento ou ataque
        self.correndo = False
        self.defender = False
        #self.attacking = False


        #teclas precionadas
        key = pygame.key.get_pressed()

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
                self.vel_y = -150
                self.jump = True
                self.movimento_atual = 'PULANDO' 
                
            # Agachar
            if key[pygame.K_s] and not self.agachar:
                self.vel_y = 100
                self.rect = pygame.Rect((self.rect.x, self.rect.y, 80, 180))
                self.agachar = True 

            #ataque
            if key[pygame.K_r] or key[pygame.K_t]:
                ataque_executado = self.attack(surface, target) # Checar se o ataque foi executado
                if ataque_executado:
                    # Inicia a animação de ataque do primeiro frame
                    self.attacking = True
                    self.movimento_atual = 'SOCANDO'
                    self.frame = 0
                    self.ultimo_update = pygame.time.get_ticks()
                    #determinando qual tipo de ataque será usado
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
            # Defesa
            elif key[pygame.K_e]:
                self.defender = True
        
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
        if self.rect.right + dx > LARGURA:
            dx = LARGURA - self.rect.right
        if self.rect.bottom + dy > HEIGHT - 230:
            self.vel_y = 0
            self.jump = False
            dy = HEIGHT - 230 - self.rect.bottom

        #atualiza a posição do jogador:
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        # Variáveis para checar o tempo entre ataques
        agora_ataque = pygame.time.get_ticks()
        elapsed_ticks_ataque = agora_ataque - self.ultimo_ataque
    
        if elapsed_ticks_ataque >= self.frame_ticks_ataque:
            self.ultimo_ataque = agora_ataque
            # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
            if self.virar == False:
                attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
            else:
                attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
            hits = attacking_rect.colliderect(target)
            self.attacking = True
            if hits:
                if target.defender == False:
                    target.health -= 2 * (len(self.animacoes['SOCANDO'])) // 2 # Dano é propocional ao tamano da animação

                    # Se o usuário estiver sem vida, indicar isso
                    if target.health <= 0:
                        target.health = 0
                        self.vencendo = True
                        target.morto = True
                else:
                    target.health += 0
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            
            return True # Retorna True se o ataque não tiver em cooldown
        else:
            return False

    # Método para desenhar o jogador
    def draw(self, surface):
        imagem_ajustada = pygame.transform.flip(self.imagem, self.virar, False)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(imagem_ajustada, (self.rect.x, self.rect.y))
    
    # Método para atualizar a animação do jogador
    def update(self):
        # Ataque precisa ser um caso especial, mesmo se não estiver 
        # atacando a animação precisa ir até o final
        if self.movimento_atual == 'SOCANDO':
            agora = pygame.time.get_ticks()
            tempo = agora - self.ultimo_update

            # Atualiza a imagem atual do frame
            self.imagem = self.animacoes[self.movimento_atual][self.frame]

            if tempo > self.frame_ticks_animacao:
                self.ultimo_update = agora
                self.frame += 1
                # se passou do último frame da animação de soco
                #  a animação acaba e o estado reseta
                if self.frame >= len(self.animacoes[self.movimento_atual]):
                    self.attacking = False
                    self.movimento_atual = 'PARADO'
                    self.frame = 0
                    self.ultimo_update = agora
            return # Para a função update()
    
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
        elif self.agachar:
            if self.movimento_atual != 'AGACHANDO':
                self.movimento_atual = 'AGACHANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.morto:
            if self.movimento_atual != 'MORTO':
                self.movimento_atual = 'MORTO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.vencendo:
            if self.movimento_atual != 'VENCENDO':
                self.movimento_atual = 'VENCENDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.jump:
            if self.movimento_atual != 'PULANDO':
                self.movimento_atual = 'PULANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        if not self.agachar:
            self.rect = pygame.Rect((self.rect.x, self.rect.y, 80, 180))

        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        # Garantir que o frame da animação está dentro dos limites antes o indíce
        num_frames = len(self.animacoes[self.movimento_atual])
        if self.frame >= num_frames:
            self.frame = 0
        
        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        if tempo > self.frame_ticks_animacao:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= num_frames:
                self.frame = 0

# Classe para o player 2 (mesma coisa que o P1, mas com teclas de movimento e ataque diferentes)
class Player2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets):
        pygame.sprite.Sprite.__init__(self)

        #variaveis que indicam o movimento
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.attack_type = 0
        self.health = 100
        self.virar = False
        self.agachar = False
        self.defender = False
        self.morto = False
        self.vencendo = False
        
        # Variáveis de animação
        self.animacoes = assets
        self.movimento_atual = 'PARADO'
        self.frame = 0
        self.imagem = assets[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
        self.ultimo_update = pygame.time.get_ticks()

        self.frame_ticks_animacao = 150  # Tempo entre frames
        
        # Só será possível atacar a cada 200 milissegundos
        self.ultimo_ataque = pygame.time.get_ticks()  # Cooldown para o ataque
        self.frame_ticks_ataque = 150 * (len(assets['SOCANDO']) + 1)  # Tempo entre ataques (50 ms para cada frame de animação)

    def move(self, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        self.vel_y = 0

        # Essas duas precisam ser falsas para atualizar a animação se o jogador soltar as teclas de movimento ou ataque
        self.correndo = False
        self.defender = False
        #self.attacking = False


        #teclas precionadas
        key = pygame.key.get_pressed()

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
                self.vel_y = -150
                self.jump = True
                self.movimento_atual = 'PULANDO' 
                
            # Agachar
            if key[pygame.K_DOWN] and not self.agachar:
                self.vel_y = 100
                self.rect = pygame.Rect((self.rect.x, self.rect.y, 80, 180))
                self.agachar = True 

            #ataque
            if key[pygame.K_RSHIFT] or key[pygame.K_KP0]:
                ataque_executado = self.attack(surface, target) # Checar se o ataque foi executado
                if ataque_executado:
                    # Inicia a animação de ataque do primeiro frame
                    self.attacking = True
                    self.movimento_atual = 'SOCANDO'
                    self.frame = 0
                    self.ultimo_update = pygame.time.get_ticks()
                    #determinando qual tipo de ataque será usado
                    if key[pygame.K_RSHIFT]:
                        self.attack_type = 1
                    if key[pygame.K_KP0]:
                        self.attack_type = 2
            # Defesa
            elif key[pygame.K_KP1]:
                self.defender = True
        
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
        if self.rect.right + dx > LARGURA:
            dx = LARGURA- self.rect.right
        if self.rect.bottom + dy > HEIGHT - 230:
            self.vel_y = 0
            self.jump = False
            dy = HEIGHT - 230 - self.rect.bottom

        #atualiza a posição do jogador:
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        # Variáveis para checar o tempo entre ataques
        agora_ataque = pygame.time.get_ticks()
        elapsed_ticks_ataque = agora_ataque - self.ultimo_ataque
    
        if elapsed_ticks_ataque >= self.frame_ticks_ataque:
            self.ultimo_ataque = agora_ataque
            # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
            if self.virar == False:
                attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
            else:
                attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
            hits = attacking_rect.colliderect(target)
            self.attacking = True
            if hits:
                if target.defender == False:
                    target.health -= 2 * (len(self.animacoes['SOCANDO'])) // 2 # Dano é propocional ao tamano da animação

                    # Se o usuário estiver sem vida, indicar isso
                    if target.health <= 0:
                        target.health = 0
                        self.vencendo = True
                        target.morto = True
                else:
                    target.health += 0
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            
            return True # Retorna True se o ataque não tiver em cooldown
        else:
            return False

    # Método para desenhar o jogador
    def draw(self, surface):
        imagem_ajustada = pygame.transform.flip(self.imagem, self.virar, False)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(imagem_ajustada, (self.rect.x, self.rect.y))
    
    # Método para atualizar a animação do jogador
    def update(self):
        # Ataque precisa ser um caso especial, mesmo se não estiver 
        # atacando a animação precisa ir até o final
        if self.movimento_atual == 'SOCANDO':
            agora = pygame.time.get_ticks()
            tempo = agora - self.ultimo_update

            # Atualiza a imagem atual do frame
            self.imagem = self.animacoes[self.movimento_atual][self.frame]

            if tempo > self.frame_ticks_animacao:
                self.ultimo_update = agora
                self.frame += 1
                # se passou do último frame da animação de soco
                #  a animação acaba e o estado reseta
                if self.frame >= len(self.animacoes[self.movimento_atual]):
                    self.attacking = False
                    self.movimento_atual = 'PARADO'
                    self.frame = 0
                    self.ultimo_update = agora
            return # Para a função update()
    
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
        elif self.agachar:
            if self.movimento_atual != 'AGACHANDO':
                self.movimento_atual = 'AGACHANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.morto:
            if self.movimento_atual != 'MORTO':
                self.movimento_atual = 'MORTO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.vencendo:
            if self.movimento_atual != 'VENCENDO':
                self.movimento_atual = 'VENCENDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        elif self.jump:
            if self.movimento_atual != 'PULANDO':
                self.movimento_atual = 'PULANDO'
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        if not self.agachar:
            self.rect = pygame.Rect((self.rect.x, self.rect.y, 80, 180))

        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        # Garantir que o frame está dentro dos limites antes de acessar
        num_frames = len(self.animacoes[self.movimento_atual])
        if self.frame >= num_frames:
            self.frame = 0
        
        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        if tempo > self.frame_ticks_animacao:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= num_frames:
                self.frame = 0

# Função para carregar o fundo do jogo
def desenha_fundo():
    fundo_escalado = pygame.transform.scale(fundo_jogo, (LARGURA, ALTURA))
    tela.blit(fundo_escalado, (0,0))

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

# função para criar a barra de vida
def desenha_barra_de_vida(health,x,y):
    ratio = health / 100
    pygame.draw.rect(tela,AMARELO, (x,y,400, 30))
    pygame.draw.rect(tela,VERMELHO, (x, y ,400 * ratio ,30))

def game_screen(screen, p1, p2):
    clock = pygame.time.Clock()
    desenha_fundo()

    try:
        pygame.mixer.music.load(path.join(MUSICAS_DIR, 'Tela do jogo.ogg'))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
    except Exception:
        pass

    player1 = Player1(200, 400, imagens_personagens[p1])
    player2 = Player2(700, 400, imagens_personagens[p2])

    state = GAME

    # Variáveis para controlar a animação de vencer e morrer
    fim_jogo = False
    fim_jogo_tempo = 0
    fim_jogo_tempo_max = 8000

    while state == GAME:
        clock.tick(FPS)
        desenha_fundo()

        desenha_barra_de_vida(player1.health, 20, 20)
        desenha_barra_de_vida(player2.health, 580, 20)

        # Só permitir inputs se os dois jogadores estiverem vivos
        if fim_jogo == False:
            player1.move(tela, player2)
            player2.move(tela, player1)

        # Sempre desenha e atualiza os players
        player1.draw(tela)
        player2.draw(tela)
        player1.update()
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            
            # Ignorar inputs normais durante fim de round
            if fim_jogo:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_s):
                    player1.move(tela, player2)
                if event.key in (pygame.K_r, pygame.K_t):
                    player1.attack(tela, player2)
                if event.key in (pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT):
                    player2.move(tela, player1)
                if event.key in (pygame.K_RSHIFT, pygame.K_KP0):
                    player2.attack(tela, player1)

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_r, pygame.K_t):
                    player1.attacking = False
                if event.key == pygame.K_s:
                    player1.agachar = False
                if event.key in (pygame.K_RSHIFT, pygame.K_KP0):
                    player2.attacking = False
                if event.key == pygame.K_DOWN:
                    player2.agachar = False

        # Vê quando o fim do round começa
        if fim_jogo == False:
            if player1.health <= 0 or player2.health <= 0:
                fim_jogo = True
                fim_jogo_tempo = pygame.time.get_ticks()
                if player1.health <= 0:
                    ganhador = 2
                    player1.health = 0
                    player1.morto = True
                    player1.movimento_atual = 'MORTO'
                    player1.frame = 0
                    player1.ultimo_update = pygame.time.get_ticks()
                    player2.vencendo = True
                    player2.movimento_atual = 'VENCENDO'
                    player2.frame = 0
                    player2.ultimo_update = pygame.time.get_ticks()
                else:
                    ganhador = 1
                    player2.health = 0
                    player2.morto = True
                    player2.movimento_atual = 'MORTO'
                    player2.frame = 0
                    player2.ultimo_update = pygame.time.get_ticks()
                    player1.vencendo = True
                    player1.movimento_atual = 'VENCENDO'
                    player1.frame = 0
                    player1.ultimo_update = pygame.time.get_ticks()

                player1.attacking = False
                player2.attacking = False
                pygame.mixer.music.stop()

        # se no final da rodada: aguarda animação terminar (MORTO) ou timeout
        if fim_jogo:
            agora = pygame.time.get_ticks()
            animacao_fim = False
            # checar com segurança as listas de frames
            if ganhador == 1:
                frames_morto = player2.animacoes['MORTO']
                if player2.frame >= len(frames_morto) - 1:
                    animacao_fim = True
            elif ganhador == 2:
                frames_morto = player1.animacoes['MORTO']
                if player1.frame >= len(frames_morto) - 1:
                    animacao_fim = True

            if animacao_fim or (agora - fim_jogo_tempo) >= fim_jogo_tempo_max:
                state = GAME_OVER

        pygame.display.update()

    return [state, ganhador]
