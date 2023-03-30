import pygame as pg
from settings import *

#BARRA DE HP/SAÚDE
class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    #ATUALIZAR NA TELA
    def draw(self, hp, screenMatch):
        self.hp = hp

        #CÁLCULO DO HP
        ratio = self.hp / self.max_hp
        pg.draw.rect(screenMatch, (255, 0, 0), (self.x, self.y, 150, 20))
        pg.draw.rect(screenMatch, (0, 255, 0), (self.x, self.y, 150 * ratio, 20))