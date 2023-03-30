import pygame as pg
from settings import *

#CLASSE DOS INIMIGOS
class Enemy():
    def __init__(self, pos, name, max_hp, strength, defense, velocity):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.defense = defense
        self.velocity = velocity
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pg.time.get_ticks()

        #MOVIMENTO PADRÃO
        temp_list = []
        for i in range(4):
            img = pg.image.load(f'imgs/{self.name}/Idle/{i}.png')
            img = pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #MOVIMENTO DE ATAQUE
        temp_list = []
        for i in range(8):
            img = pg.image.load(f'imgs/{self.name}/Attack/{i}.png')
            img = pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        #MOVIMENTO DE DANO
        temp_list = []
        for i in range(4):
            img = pg.image.load(f'imgs/{self.name}/TakeHit/{i}.png')
            img = pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #MOVIMENTO DA MORTE
        temp_list = []
        for i in range(4):
            img = pg.image.load(f'imgs/{self.name}/Death/{i}.png')
            img = pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #ANIMAÇÃO
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

    #CARREGAR IMAGENS/ANIMAÇÃO NA TELA
    def update(self):
        #TEMPO DA ANIMAÇÃO
        animation_cooldown = 80

        #ATUALIZAR IMAGENS/ANIMAÇÃO
        self.image = self.animation_list[self.action][self.frame_index]

        #CHECAR ATUALIZAÇÕES
        if pg.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

        #REINICIALIZAÇÃO DAS IMAGENS/ANIMAÇÃO
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    #MOVIMENTAÇÃO CONSTANTE
    def idle(self):
        #VARIÁVLE PARA ANIMAÇÃO
        self.action = 0
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

    #MOVIMENTAÇÃO DE ATAQUE
    def attack(self, target):
        damage = self.strength * (50 / (50 + target.defense))
        if damage > target.hp:
            damage = target.hp
        target.hp -= int(damage)
        target.hurt()

        #CHECAGEM SE ALVO AINDA ESTÁ VIVO
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()

        #VARIÁVLE PARA ANIMAÇÃO
        self.action = 1
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()
    
    #MOVIMENTAÇÃO DE DANO TOMADO
    def hurt(self):
        #VARIÁVLE PARA ANIMAÇÃO
        self.action = 2
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

    #MOVIMENTAÇÃO DE MORTE
    def death(self):
        #VARIÁVLE PARA ANIMAÇÃO
        self.action = 3
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

    #ATUALIZAR NA TELA
    def draw(self, screenMatch):
        screenMatch.blit(self.image, self.rect)