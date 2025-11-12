# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from declarações_importantes import *
from tela_de_selecao import *

# Classe do Player 1
class Player1(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets, nome):
        pygame.sprite.Sprite.__init__(self)

        #variaveis que indicam o movimento
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y, 80, 160))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.health = 100
        self.virar = False
        self.agachar = False
        self.defender = False
        self.morto = False
        self.vencendo = False
        self.nome = nome 
        
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
        self.frame_ticks_ataque = 150 * (len(assets['ATACANDO']) + 1)  # Tempo entre ataques (50 ms para cada frame de animação)
        
        # Cooldown para especiais
        self.ultimo_especial = pygame.time.get_ticks()
        self.cooldown_especial = 5000  # Cooldown entre especiais

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

        if self.attacking == False and self.agachar == False:
            #movimentos
            if key[pygame.K_a]:
                dx = -SPEED
                self.correndo = True
            if key[pygame.K_d]:
                dx = SPEED
                self.correndo = True

            #pular
            if key[pygame.K_w] and not self.jump:
                self.vel_y = -200
                self.jump = True
                self.movimento_atual = 'PULANDO' 
                
            # Agachar
            if key[pygame.K_s] and not self.agachar:
                self.vel_y = 100
                pé = self.rect.bottom
                self.rect.height = 100
                self.rect.bottom = pé
                self.agachar = True 

            # Ataque comum
            if key[pygame.K_r]:
                ataque_executado = self.attack(surface, target) # Checar se o ataque foi executado
                if ataque_executado:
                    # Inicia a animação de ataque do primeiro frame
                    self.attacking = True
                    self.movimento_atual = 'ATACANDO'
                    self.frame = 0
                    self.ultimo_update = pygame.time.get_ticks()
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
            # Calcula a posição Y do peito (3/4 da altura do personagem)
            peito_y = self.rect.top + (self.rect.height) // 4
            # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
            if self.virar == False:
                attacking_rect = pygame.Rect(self.rect.centerx, peito_y, self.rect.width, 32)
            else:
                attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, peito_y, self.rect.width, 32)
            hits = attacking_rect.colliderect(target.rect)
            self.attacking = True
            if hits:
                #O julien agora vai dar hitkill
                if target.defender == False:
                    if self.nome == 'julien':
                        target.health = 0

                    else:
                        target.health -= (3 * len(self.animacoes['ATACANDO'])) // 2 # Dano é propocional ao tamanho da animação

                    # Se o usuário estiver sem vida, indicar isso
                    if target.health <= 0:
                        target.health = 0
                        self.vencendo = True
                        target.morto = True
                else:
                    target.health += 0
            
            return True # Retorna True se o ataque não tiver em cooldown
        else:
            return False
    
    def shoot(self, especiais_group, target, sprite_especial):
        # Verifica cooldown
        agora = pygame.time.get_ticks()
        elapsed = agora - self.ultimo_especial
        
        if elapsed >= self.cooldown_especial:
            self.ultimo_especial = agora
            # Especial será lançado do centro do personagem
            x = self.rect.centerx
            y = self.rect.centery
            # Direção determinada por self.virar
            direcao = self.virar
            
            # Criar e adicionar o especial ao grupo
            novo_especial = especial(x, y, direcao, target, sprite_especial)
            especiais_group.add(novo_especial)
            return True
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
        if self.movimento_atual == 'ATACANDO':
            agora = pygame.time.get_ticks()
            tempo = agora - self.ultimo_update

            # Atualiza a imagem atual do frame
            self.imagem = self.animacoes[self.movimento_atual][self.frame]
            self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))

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
            if self.movimento_atual != 'ATACANDO':
                self.movimento_atual = 'ATACANDO'
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
        elif self.defender:
            if self.movimento_atual != 'DEFENDENDO':
                self.movimento_atual = "DEFENDENDO"
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        if not self.agachar:
            pé = self.rect.bottom
            self.rect.height = 160
            self.rect.bottom = pé

        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        # Garantir que o frame da animação está dentro dos limites antes o indíce
        num_frames = len(self.animacoes[self.movimento_atual])
        if self.frame >= num_frames:
            self.frame = 0
        
        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        if tempo > self.frame_ticks_animacao:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= num_frames:
                self.frame = 0

# Classe para o player 2 (mesma coisa que o P1, mas com teclas de movimento e ataque diferentes)
class Player2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, assets, nome):
        pygame.sprite.Sprite.__init__(self)

        #variaveis que indicam o movimento
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y, 80, 160))
        self.vel_y = 0
        self.jump = False
        self.attacking = False 
        self.correndo = False
        self.health = 100
        self.virar = False
        self.agachar = False
        self.defender = False
        self.morto = False
        self.vencendo = False
        self.nome = nome 
        
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
        self.frame_ticks_ataque = 150 * (len(assets['ATACANDO']) + 1)  # Tempo entre ataques (50 ms para cada frame de animação)
        
        # Cooldown para especiais
        self.ultimo_especial = pygame.time.get_ticks()
        self.cooldown_especial = 5000  # Cooldown entre especiais

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

        if self.attacking == False and self.agachar == False:
            #movimentos
            if key[pygame.K_LEFT]:
                dx = -SPEED
                self.correndo = True
            if key[pygame.K_RIGHT]:
                dx = SPEED
                self.correndo = True

            #pular
            if key[pygame.K_UP] and not self.jump:
                self.vel_y = -200
                self.jump = True
                self.movimento_atual = 'PULANDO' 
                
            # Agachar
            if key[pygame.K_DOWN] and not self.agachar:
                self.vel_y = 100
                pé = self.rect.bottom
                self.rect.height = 100
                self.rect.bottom = pé
                self.agachar = True 

            # Ataque comum
            if key[pygame.K_RSHIFT]:
                ataque_executado = self.attack(surface, target) # Checar se o ataque foi executado
                if ataque_executado:
                    # Inicia a animação de ataque do primeiro frame
                    self.attacking = True
                    self.movimento_atual = 'ATACANDO'
                    self.frame = 0
                    self.ultimo_update = pygame.time.get_ticks()
            # Defesa
            elif key[pygame.K_KP0]:
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
            # Calcula a posição Y do peito (3/4 da altura do personagem)
            peito_y = self.rect.top + (self.rect.height) // 4
            # Se o jogador estiver virado para o oponente ele ataca pra direita, se não para a esquerda
            if self.virar == False:
                attacking_rect = pygame.Rect(self.rect.centerx, peito_y, self.rect.width, 32)
            else:
                attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, peito_y, self.rect.width, 32)
            hits = attacking_rect.colliderect(target.rect)
            self.attacking = True
            if hits:
                #O julien agora vai dar hitkill
                if target.defender == False:
                    if self.nome == 'julien':
                        target.health = 0
                        
                    else:
                        target.health -= (3 * len(self.animacoes['ATACANDO'])) // 2 # Dano é propocional ao tamanho da animação

                    # Se o usuário estiver sem vida, indicar isso
                    if target.health <= 0:
                        target.health = 0
                        self.vencendo = True
                        target.morto = True
                else:
                    target.health += 0
            
            return True # Retorna True se o ataque não tiver em cooldown
        else:
            return False
    
    def shoot(self, especiais_group, target, sprite_especial):
        # Verifica cooldown
        agora = pygame.time.get_ticks()
        elapsed = agora - self.ultimo_especial
        
        if elapsed >= self.cooldown_especial:
            self.ultimo_especial = agora
            # Especial será lançado do centro do personagem
            x = self.rect.centerx
            y = self.rect.centery
            # Direção determinada por self.virar
            direcao = self.virar
            
            # Criar e adicionar o especial ao grupo
            novo_especial = especial(x, y, direcao, target, sprite_especial)
            especiais_group.add(novo_especial)
            return True
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
        if self.movimento_atual == 'ATACANDO':
            agora = pygame.time.get_ticks()
            tempo = agora - self.ultimo_update

            # Atualiza a imagem atual do frame
            self.imagem = self.animacoes[self.movimento_atual][self.frame]
            self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))

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
            if self.movimento_atual != 'ATACANDO':
                self.movimento_atual = 'ATACANDO'
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
        elif self.defender:
            if self.movimento_atual != 'DEFENDENDO':
                self.movimento_atual = "DEFENDENDO"
                self.frame = 0
                self.ultimo_update = pygame.time.get_ticks()
        else:
            # Se o jogador não está se movendo, a animação muda para parado
            if self.movimento_atual != 'PARADO':
                self.movimento_atual = 'PARADO'
                self.frame = 0
        if not self.agachar:
            pé = self.rect.bottom
            self.rect.height = 160
            self.rect.bottom = pé

        # Controle de frames da animação
        agora = pygame.time.get_ticks()
        tempo = agora - self.ultimo_update

        # Garantir que o frame da animação está dentro dos limites antes o indíce
        num_frames = len(self.animacoes[self.movimento_atual])
        if self.frame >= num_frames:
            self.frame = 0
        
        self.imagem = self.animacoes[self.movimento_atual][self.frame]
        self.imagem = pygame.transform.scale(self.imagem, (self.rect.width, self.rect.height))
        if tempo > self.frame_ticks_animacao:
            self.ultimo_update = agora
            self.frame += 1
            if self.frame >= num_frames:
                self.frame = 0

# Classe do especial
class especial(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao, target, sprite):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 10
        self.direcao = direcao
        self.target = target
        self.image = sprite
        
        # Ajustar a direção do especial
        if direcao:
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
    def update(self):
        # Lança o especial sem gravidade
        if self.direcao:  
            self.rect.x -= self.speed
        else:  # Direita
            self.rect.x += self.speed
        
        # Remove o projétil se sair da tela
        if self.rect.right < 0 or self.rect.left + self.speed > LARGURA:
            self.kill()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

def desenha_barra_de_especial(player, tela, x, y, largura_max=200, altura=20):
    # 1. Calcular o 'ratio' (porcentagem de recarga)
    agora = pygame.time.get_ticks()
    elapsed = agora - player.ultimo_especial
    total_cooldown = player.cooldown_especial
    
    ratio = min(1.0, elapsed / total_cooldown)

    cor_barra = AZUL
    if ratio >= 1.0:
        cor_barra = VERDE
        
    largura_atual = largura_max * ratio

    pygame.draw.rect(tela, PRETO, (x, y, largura_max, altura)) 
    pygame.draw.rect(tela, cor_barra, (x, y, largura_atual, altura)) 
    pygame.draw.rect(tela, BRANCO, (x, y, largura_max, altura), 2)

def game_screen(screen, p1, p2):
    clock = pygame.time.Clock()
    desenha_fundo()

    pygame.mixer.music.load(path.join(MUSICAS_DIR, 'Tela do jogo.ogg'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    player1 = Player1(200, 400, imagens_personagens[p1], p1)
    player2 = Player2(700, 400, imagens_personagens[p2], p2)

    # Grupo de sprites para os projéteis
    especiais = pygame.sprite.Group()

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

        desenha_barra_de_especial(player1, tela, 20, 55, 200, 20) 
        x_p2 = 580 + 400 - 200 
        desenha_barra_de_especial(player2, tela, x_p2, 55, 200, 20)

        # Só permitir inputs se os dois jogadores estiverem vivos
        if fim_jogo == False:
            player1.move(tela, player2)
            player2.move(tela, player1)

        # Sempre desenha e atualiza os players
        player1.update()
        player2.update()
        player1.draw(tela)
        player2.draw(tela)

        # Atualizar e desenhar projéteis
        especiais.update()
        for especial in especiais:
            especial.draw(tela)
            
            # Verificar colisão com o target
            if pygame.sprite.collide_rect(especial, especial.target):
                # Especial acertou o target
                if especial.target.defender == False:
                    especial.target.health -= 20  
                    # Se o target estiver morto
                    if especial.target.health <= 0:
                        especial.target.health = 0
                        if especial.target == player1:
                            player2.vencendo = True
                            player1.morto = True
                        else:
                            player1.vencendo = True
                            player2.morto = True
                especial.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            
            # Ignorar inputs normais durante fim de round
            if fim_jogo:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_s):
                    player1.move(tela, player2)
                if event.key == pygame.K_r:
                    player1.attack(tela, player2)
                if event.key == pygame.K_t:
                    player1.shoot(especiais, player2, imagens_personagens[p1]['ESPECIAL'])
                if event.key in (pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT):
                    player2.move(tela, player1)
                if event.key == pygame.K_RSHIFT:
                    player2.attack(tela, player1)
                if event.key == pygame.K_KP1:
                    player2.shoot(especiais, player1, imagens_personagens[p2]['ESPECIAL'])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    player1.attacking = False
                if event.key == pygame.K_s:
                    player1.agachar = False
                if event.key == pygame.K_RSHIFT:
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