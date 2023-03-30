#BIBLIOTECAS BÁSICAS*********************************************************************************************
import pygame as pg
from enemy import Enemy
from fighter import Fighter
from healthPlayer import HealthBar
global bgMatch, screenMatch, pos1, pos2, pos3, posEnemy1, posEnemy2, selection, playersSelecteds

#INICIALIZAÇÃO PYGAME********************************************************************************************
pg.init()

#CONFIGURÇÕES BÁSICAS********************************************************************************************
pg.display.set_caption('INTROGAME')
clock = pg.time.Clock()
fps = 60

#VARIÁVEIS PARA VERIFICAÇÃO**************************************************************************************
currentFighter = 1
totalFighters = 5
lastPlayer = 0
actionCooldown = 0
actionWaitTime = 80
attack = False
target = None

#DIMENÇÕES DA TELA INICIAL***************************************************************************************
width = 1280
height = 720

#CARREGANDO TELA E FUNDO INICIAL*********************************************************************************
screen = pg.display.set_mode((width, height))
bg = pg.image.load("imgs/bg.png")
bg = pg.transform.scale(bg, (width, height))

#DIMENÇÕES DA TELA SECUNDÁRIA************************************************************************************
bottomPanel = 150
screenWidth = 1280
screenHeight = 570 + bottomPanel

#CARREGANDO TELA E FUNDO SECUNDÁRIO******************************************************************************
screenMatch = pg.display.set_mode((screenWidth, screenHeight))
bgMatch = pg.image.load('imgs/bg.png').convert_alpha()
bgMatch = pg.transform.scale(bgMatch, (1280, 570))
panelImg = pg.image.load('imgs/panel.png').convert_alpha()
panelImg = pg.transform.scale(panelImg, (1280, 150))

#VARIÁVEIS DE SELEÇÃO********************************************************************************************
selection = []
playersSelecteds = [[], []]

#POSIÇÕES DOS INIMIGOS*******************************************************************************************
posEnemy1 = 980, 220
posEnemy2 = 1000,390

#VARIÁVEIS DOS INIMIGOS******************************************************************************************
enemy1 = Enemy(posEnemy1, 'GOBLIN', 150, 30, 10, 2)
enemy1HealthBar = HealthBar(895, screenHeight - bottomPanel + 17, enemy1.hp, enemy1.max_hp)
enemy2 = Enemy(posEnemy2, 'SKELETON', 140, 30, 10, 2)
enemy2HealthBar = HealthBar(925, screenHeight - bottomPanel + 78, enemy2.hp, enemy2.max_hp)
enemyList = [enemy1, enemy2]

#SOM DE FUNDO****************************************************************************************************
pg.mixer.init()
bgMusic = pg.mixer.music.load("sounds/sound.wav")
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)

#CARREGAR IMAGEM DO MOUSE****************************************************************************************
swordImg = pg.image.load('imgs/sword.png').convert_alpha()

#FONTE UTILIZADA*************************************************************************************************
def font(size):
    return pg.font.Font("imgs/font.ttf", size)

#ATUALIZAR FUNDO*************************************************************************************************
def drawBg():
    return screenMatch.blit(bgMatch, (0, 0))

#TEXTO MAIS PRÁTICO**********************************************************************************************
def text(textInput, font, text_col, x, y):
    text = font.render(textInput, True, text_col)
    screen.blit(text, (x, y))

#TRANFORMAR ESCALA DA IMAGEM*************************************************************************************
def trasformScale(image, scale_x, scale_y):
	return pg.transform.scale(image, (scale_x, scale_y))

#IMAGENS MAIS FÁCEIS*********************************************************************************************
def image(ref, scale_x, scale_y, pos):
	image = pg.image.load(ref)
	image = pg.transform.scale(image, (scale_x, scale_y))
	screen.blit(image, (pos[0], pos[1]))

#CARREGAR PAINEL NA TELA*****************************************************************************************
def drawPanel():
    #ATUALIZAR PAINEL
    screenMatch.blit(panelImg, (0, screenHeight - bottomPanel))

    #ATUALIZAR INFORMAÇÕES DE SAÚDE DOS PERSONAGENS (VERIFICAR)
    for count, i in enumerate(playersSelecteds[0]):
        text(f'{i.name} HP: {i.hp}', font(15), "Black", 50, (screenHeight - bottomPanel + 22) + count * 45)

    #ATUALIZAR INFORMAÇÕES DE SAÚDE DOS INIMIGOS
    for count, i in enumerate(enemyList):
        text(f'{i.name} HP: {i.hp}', font(15), "Black", 680, (screenHeight - bottomPanel + 22) + count * 60)

#VERIFICAÇÃO DO TURNO DOS PERSONAGENS***************************************************************************
def turn1():
	if playersSelecteds[0][0].name == "PALADINO":
		image("imgs/PaladinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][0].name == "ASSASSINA":
		image("imgs/AssassinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][0].name == "MAGO":
		image("imgs/WizardTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][0].name == "ARQUEIRO":
		image("imgs/ArchTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][0].name == "MONGE":
		image("imgs/MonkTurn.png", 600, 80, (350, 10))

def turn2():
	image("imgs/GoblinTurn.png", 600, 80, (350, 10))

def turn3():
	if playersSelecteds[0][1].name == "PALADINO":
		image("imgs/PaladinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][1].name == "ASSASSINA":
		image("imgs/AssassinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][1].name == "MAGO":
		image("imgs/WizardTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][1].name == "ARQUEIRO":
		image("imgs/ArchTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][1].name == "MONGE":
		image("imgs/MonkTurn.png", 600, 80, (350, 10))

def turn4():
	image("imgs/SkeletonTurn.png", 600, 80, (350, 10))

def turn5():
	if playersSelecteds[0][2].name == "PALADINO":
		image("imgs/PaladinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][2].name == "ASSASSINA":
		image("imgs/AssassinTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][2].name == "MAGO":
		image("imgs/WizardTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][2].name == "ARQUEIRO":
		image("imgs/ArchTurn.png", 600, 80, (350, 10))
	if playersSelecteds[0][2].name == "MONGE":
		image("imgs/MonkTurn.png", 600, 80, (350, 10))

#ORGANIZAÇÃO DA LISTA DE PERSONAGENS SELECIONADOS****************************************************************
def updateCharsInfo():
	for player in selection:

		if player == selection[0]:
			posX = 330
			posY = 180
			posH = 250
			posB = 588
		if player == selection[1]:
			posX = 500
			posY = 300
			posH = 250
			posB = 633
		if player == selection[2]:
			posX = 350
			posY = 420
			posH = 250
			posB = 678

		if player == "PALADINO":
			paladin = Fighter((posX, posY), 'PALADINO', 130, 15, 50, 2)
			paladinHealthBar = HealthBar(posH + 45, posB, paladin.hp, paladin.max_hp)
			try:
				playersSelecteds[0].append(paladin)
				playersSelecteds[1].append(paladinHealthBar)
			except ValueError as r:
				print(r)
				raise r

		if player == "ASSASSINA":
			assassin = Fighter((posX - 50, posY - 150), 'ASSASSINA', 120, 25, 15, 2)
			assassinHealthBar = HealthBar(posH + 60, posB, assassin.hp, assassin.max_hp)
			try:
				playersSelecteds[0].append(assassin)
				playersSelecteds[1].append(assassinHealthBar)
			except ValueError as r:
				print(r)
				raise r
		
		if player == "MAGO":
			wizard = Fighter((posX - 35, posY), 'MAGO', 115, 30, 10, 2)
			wizardHealthBar = HealthBar(posH - 15, posB, wizard.hp, wizard.max_hp)
			try:
				playersSelecteds[0].append(wizard)
				playersSelecteds[1].append(wizardHealthBar)
			except ValueError as r:
				print(r)
				raise r
		
		if player == "ARQUEIRO":
			archer = Fighter((posX, posY - 150), 'ARQUEIRO', 120, 20, 15, 2)
			archerHealthBar = HealthBar(posH + 45, posB, archer.hp, archer.max_hp)
			try:
				playersSelecteds[0].append(archer)
				playersSelecteds[1].append(archerHealthBar)
			except ValueError as r:
				print(r)
				raise r
		
		if player == "MONGE":
			monk = Fighter((posX - 20, posY - 150), 'MONGE', 125, 10, 30, 2)
			monkHealthBar = HealthBar(posH, posB, monk.hp, monk.max_hp)
			try:
				playersSelecteds[0].append(monk)
				playersSelecteds[1].append(monkHealthBar)
			except ValueError as r:
				print(r)
				raise r

#BOTÕES*********************************************************************************************************
class Button():
	def __init__(self, image, pos, textInput, font, baseColor, hoveringColor):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.baseColor, self.hoveringColor = baseColor, hoveringColor
		self.textInput  = textInput
		self.text = self.font.render(self.textInput, True, self.baseColor)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #CARREGAR IMAGEM
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
		
    #CHECAR PARA O INPUT
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

    #MUDANÇA DE COR AO PASSAR O MOUSE
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.textInput, True, self.hoveringColor)
		else:
			self.text = self.font.render(self.textInput, True, self.baseColor)