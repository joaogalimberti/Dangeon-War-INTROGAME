#BIBLIOTECAS****************************************************************************************************
import pygame as pg
from settings import *

#JOGO***********************************************************************************************************
class Game():
    def __init__(self, screen, bg):
        self.screen = screen
        self.bg = bg
        

    #TELA DO MENU***********************************************************************************************
    def mainMenu(self, screen, bg):
        while True:
            menuMousePos = pg.mouse.get_pos()
            screen.blit(bg, (0, 0))

            #TÍTULO DO JOGO
            image("imgs/Title.png", 1000, 200, (130, 10))

            #BOTÕES DO MENU
            playButton = Button(pg.image.load("imgs/Play Rect.png"), (640, 250), "JOGAR", font(70), "#d7fcd4", "Gray")
            creditsButton = Button(pg.image.load("imgs/Options Rect.png"), (640, 400), "CRÉDITOS", font(70), "#d7fcd4", "Gray")
            quitButton = Button(pg.image.load("imgs/Quit Rect.png"), (640, 550), "SAIR", font(70), "#d7fcd4", "Gray")

            #LOOP PARA CARREGAR OS BOTÕES DO MENU
            for button in [playButton, creditsButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            
            #EVENTOS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if playButton.checkForInput(menuMousePos):
                        Game(screen, bg).play(screen)
                    if creditsButton.checkForInput(menuMousePos):
                        Game(screen, bg).credits(screen)
                    if quitButton.checkForInput(menuMousePos):
                        pg.quit()
                        exit()

            pg.display.update()
    
    #TELA DO PLAY***********************************************************************************************
    def play(self, screen):
        while True:
            playMousePos = pg.mouse.get_pos()
            screen.blit(bg, (0, 0))

            #LEGENDA
            text(f"Selecione 3 personagens", font(30), "Black", 316, 38)
            text(f"Selecione 3 personagens", font(30), "#b68f40", 320, 40)
            text(f"Clique na tecla z para confirmar", font(20), "Black", 348, 78)
            text(f"Clique na tecla z para confirmar", font(20), "#b68f40", 350, 80)

            #BOTÃO PALADINO
            text(f"PALADINO", font(10), "White", 300, 300)
            image("imgs/frame.png", 150, 150, (260, 130))
            image("imgs/PALADINO/Attack/0.png", 220, 150, (250, 120))

            #BOTÃO ASSASSINA
            text(f"ASSASSINA", font(10), "White", 590, 300)
            image("imgs/frame.png", 150, 150, (560, 130))
            image("imgs/ASSASSINA/Attack/0.png", 800, 500, (230, -225))  

            #BOTÃO MAGO
            text(f"MAGO", font(10), "White", 920, 300)
            image("imgs/frame.png", 150, 150, (860, 130))
            image("imgs/MAGO/TakeHit/0.png", 150, 150, (865, 130))            

            #BOTÃO ARQUEIRO
            text(f"ARQUEIRO", font(10), "White", 450, 520)
            image("imgs/frame.png", 150, 150, (410, 350))
            image("imgs/ARQUEIRO/Attack/5.png", 650, 320, (150, 170))

            #BOTÃO MONGE
            text(f"MONGE", font(10), "White", 765, 520)
            image("imgs/frame.png", 150, 150, (710, 350))
            image("imgs/MONGE/Attack/0.png", 1100, 400, (250, 110))

            #BOTÃO BACK NA ABA PLAY
            playBack = Button(None, (640, 600), "BACK", font(40), "White", "Gray")
            playBack.changeColor(playMousePos)
            playBack.update(screen)

            #EVENTOS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if playBack.checkForInput(playMousePos):
                        selection.clear()
                        Game(screen, bg).mainMenu(screen, bg)

                #SELEÇÃO DO PALADINO
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (len(selection) < 3) and ((playMousePos[0] >= 260) and (playMousePos[0] <= 410) and (playMousePos[1] >= 130) and (playMousePos[1] <= 280)):
                        selection.append("PALADINO")
                        
                        #REFORÇO DO BOTÃO DO PALADINO
                        pg.draw.rect(screen, (255, 248, 220), (240, 110, 190, 210))
                        image("imgs/frame.png", 150, 150, (260, 130))
                        image("imgs/PALADINO/Attack/0.png", 220, 150, (250, 120))
                
                #SELEÇÃO DA ASSASSINA
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (len(selection) < 3) and ((playMousePos[0] >= 560) and (playMousePos[0] <= 710) and (playMousePos[1] >= 130) and (playMousePos[1] <= 280)):
                        selection.append("ASSASSINA")
                        
                        #REFORÇO DO BOTÃO DA ASSASSINA
                        pg.draw.rect(screen, (255, 248, 220), (540, 110, 190, 210))
                        image("imgs/frame.png", 150, 150, (560, 130))
                        image("imgs/ASSASSINA/Attack/0.png", 800, 500, (230, -225))  
                
                #SELEÇÃO DO MAGO
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (len(selection) < 3) and ((playMousePos[0] >= 860) and (playMousePos[0] <= 1010) and (playMousePos[1] >= 130) and (playMousePos[1] <= 280)):
                        selection.append("MAGO")
                        
                        #REFORÇO DO BOTÃO DO MAGO
                        pg.draw.rect(screen, (255, 248, 220), (840, 110, 190, 210))
                        image("imgs/frame.png", 150, 150, (860, 130))
                        image("imgs/MAGO/TakeHit/0.png", 150, 150, (865, 130))
                
                #SELEÇÃO DO ARQUEIRO
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (len(selection) < 3) and ((playMousePos[0] >= 410) and (playMousePos[0] <= 560) and (playMousePos[1] >= 350) and (playMousePos[1] <= 500)):
                        selection.append("ARQUEIRO")
                        
                        #REFORÇO DO BOTÃO DO ARQUEIRO
                        pg.draw.rect(screen, (255, 248, 220), (390, 330, 190, 210))
                        image("imgs/frame.png", 150, 150, (410, 350))
                        image("imgs/ARQUEIRO/Attack/5.png", 650, 320, (150, 170))

                #SELEÇÃO DO MONGE
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (len(selection) < 3) and ((playMousePos[0] >= 710) and (playMousePos[0] <= 860) and (playMousePos[1] >= 350) and (playMousePos[1] <= 500)):
                        selection.append("MONGE")
                        
                        #REFORÇO DO BOTÃO DO MONGE
                        pg.draw.rect(screen, (255, 248, 220), (690, 330, 190, 210))
                        image("imgs/frame.png", 150, 150, (710, 350))
                        image("imgs/MONGE/Attack/0.png", 1100, 400, (250, 110))

                #CONFIRMAÇÃO DOS PERSONAGENS SELECIONADOS
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_z:
                        if len(selection) == 3:
                            updateCharsInfo()
                            Game(screen, bg).playMatch(screenMatch)

            #ATUALIZAÇÃO DA TELA
            pg.display.update()
        
    #TELA DOS CRÉDITOS*****************************************************************************************
    def credits(self, screen):
        while True:
            creditsMousePos = pg.mouse.get_pos()
            screen.blit(bg, (0, 0))

            #TEXTO DE CRÉDITOS DAS ARTES
            text(f"Artes: Augusto Moraes Alves, Bernardo Seibert, Geisson Ve-", font(20), "White", 80, 220)
            text("nancio do Nascimento, Giulia Guimaraes, Kaique Taylor Gri-", font(20), "White", 80, 250)
            text("pa dos Santos, Kiara Pezzin Silva, Raquel Paulo Silva,Rhu-", font(20), "White", 80, 290)
            text("an dos Santos,Jesse Munguia,Luiz Melo,@Clembod, @chierit7,", font(20), "White", 80, 330)
            text("@9E0_D0.", font(20), "White", 80, 370)

            #TEXTO DE CRÉDITOS DO DESENVOLVIMENTO
            text("Desenvolvimento do jogo: João Vitor Galimberti Contarato", font(20), "White", 80, 420)        

            #BOTÃO BACK NA ABA DE CRÉDITOS
            creditsBack = Button(None, (640, 600), "BACK", font(40), "White", "Gray")
            creditsBack.changeColor(creditsMousePos)
            creditsBack.update(screen)

            #EVENTOS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if creditsBack.checkForInput(creditsMousePos):
                        Game(screen, bg).mainMenu(screen, bg)

            #ATUALIZAÇÃO DA TELA
            pg.display.update()

    #TELA DA PARTIDA********************************************************************************************
    def playMatch(self, screenMatch):
        while True:
            clock.tick(fps)
            screenMatch.blit(bgMatch, (0, 0))
            pos = pg.mouse.get_pos()

            #VARIÁVEIS PARA VERIFICAÇÃO
            attack = False
            deadPlayers = 0
            deadEnemys = 0
            target = None

            #ATUALIZAR PAINEL NA TELA
            drawPanel()

            #ATUALIZAR BARRA DE HP NA TELA
            for i in range(3):
                playersSelecteds[1][i].draw(playersSelecteds[0][i].hp, screenMatch)
            
            enemy1HealthBar.draw(enemy1.hp, screenMatch)
            enemy2HealthBar.draw(enemy2.hp, screenMatch)

            #ATUALIZAR INIMIGOS NA TELA
            for enemy in enemyList:
                enemy.update()
                enemy.draw(screenMatch)

            #ATUALIZAR PERSONAGENS NA TELA
            for i in range(3):
                playersSelecteds[0][i].update()
                playersSelecteds[0][i].draw(screenMatch)
            
            #SETAR AS VARIÁVEIS COMO GLOBAIS
            global currentFighter, actionCooldown, lastPlayer, flag

            #EVENTOS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                
                #SELEÇÃO DO ALVO
                if event.type == pg.MOUSEBUTTONDOWN:
                    if ((pos[0] >= 930) and (pos[0] <= 1025) and (pos[1] >= 185) and (pos[1] <= 300)):
                        attack = True
                        target = enemyList[0]

                    if ((pos[0] >= 905) and (pos[0] <= 1040) and (pos[1] >= 300) and (pos[1] <= 470)):
                        attack = True
                        target = enemyList[1]
            
            #IMAGEM DE DERROTA
            for i in playersSelecteds[0]:
                if i.alive == False:
                    deadPlayers += 1
                if deadPlayers == 3:
                    image("imgs/bgDefeat.png", 1000, 400, (110, 110))
                    image("imgs/Defeat.png", 700, 200, (250, 200))
                else:
                    pass
                    
            #IMAGEM DE VITÓRIA
            for i in enemyList:
                if i.alive == False:
                    deadEnemys += 1
                if deadEnemys == 2:
                    image("imgs/bgDefeat.png", 1000, 400, (110, 110))
                    image("imgs/Victory.png", 700, 200, (250, 200))
                    image("imgs/legVictory.png", 500, 40, (385, 395))
                else:
                    pass

            #AÇÃO DOS PERSONAGENS
            #ATAQUE DO ALIADO 1 (JOGADOR 1)
            if playersSelecteds[0][0].alive == True:
                if currentFighter == 1 and lastPlayer != 1:
                    actionCooldown += 1
                    if actionCooldown >= (actionWaitTime - 20):
                        turn1()
                        #VERIFICAÇÃO DE AÇÃO
                        #ATAQUE
                        if (attack == True) and (target != None):
                            if target.alive != False:
                                playersSelecteds[0][0].attack(target)
                                currentFighter += 1
                                lastPlayer = 1
                                actionCooldown = 0

            elif playersSelecteds[0][0].alive == False and lastPlayer != 3:
                currentFighter = 3

            elif playersSelecteds[0][0].alive == False and lastPlayer != 2:
                currentFighter = 2

            elif playersSelecteds[0][0].alive == False and lastPlayer != 4:
                currentFighter = 4
                
            else:
                currentFighter = 5

            #ATAQUE DO INIMIGO 1 (JOGADOR 2)
            if enemyList[0].alive == True:
                if currentFighter == 2 and lastPlayer != 2:
                    actionCooldown += 1
                    if actionCooldown >= actionWaitTime:
                        turn2()
                        #VERIFICAÇÃO DE AÇÃO
                        #ATAQUE
                        if playersSelecteds[0][0].alive == True:
                            enemyList[0].attack(playersSelecteds[0][0])
                            currentFighter += 1
                            lastPlayer = 2
                            actionCooldown = 0

                        if (playersSelecteds[0][0].alive == False) and (playersSelecteds[0][1].alive == True):
                            enemyList[0].attack(playersSelecteds[0][1])
                            currentFighter += 1
                            lastPlayer = 2
                            actionCooldown = 0

                        if (playersSelecteds[0][0].alive == False) and (playersSelecteds[0][1].alive == False) and (playersSelecteds[0][2].alive == True):
                            enemyList[0].attack(playersSelecteds[0][2])
                            currentFighter += 1
                            lastPlayer = 2
                            actionCooldown = 0

            elif enemyList[0].alive == False and lastPlayer != 4:
                currentFighter = 4

            elif enemyList[0].alive == False and lastPlayer != 3:
                currentFighter = 3

            elif enemyList[0].alive == False and lastPlayer != 5:
                currentFighter = 5

            else:
                currentFighter = 1
            
            #ATAQUE DO ALIADO 2 (JOGADOR 3)
            if playersSelecteds[0][1].alive == True:
                if currentFighter == 3 and lastPlayer != 3:
                    actionCooldown += 1
                    if actionCooldown >= actionWaitTime:
                        turn3()
                        #VERIFICAÇÃO DE AÇÃO
                        #ATAQUE
                        if (attack == True) and (target != None):
                            if target.alive != False:
                                playersSelecteds[0][1].attack(target)
                            currentFighter += 1
                            lastPlayer = 3
                            actionCooldown = 0
            elif playersSelecteds[0][1].alive == False and lastPlayer != 5:
                currentFighter = 5

            elif playersSelecteds[0][1].alive == False and lastPlayer != 2:
                currentFighter = 2

            elif playersSelecteds[0][1].alive == False and lastPlayer != 4:
                currentFighter = 4
                
            else:
                currentFighter = 1
                                
            #ATAQUE DO INIMIGO 2 (JOGADOR 4)
            if enemyList[1].alive == True:
                if currentFighter == 4 and lastPlayer != 4:
                    actionCooldown += 1
                    if actionCooldown >= actionWaitTime:
                        turn4()
                        #VERIFICAÇÃO DE AÇÃO
                        #ATAQUE
                        if playersSelecteds[0][0].alive == True:
                            enemyList[1].attack(playersSelecteds[0][0])
                            currentFighter += 1
                            lastPlayer = 4
                            actionCooldown = 0

                        if (playersSelecteds[0][0].alive == False) and (playersSelecteds[0][1].alive == True):
                            enemyList[1].attack(playersSelecteds[0][1])
                            currentFighter += 1
                            lastPlayer = 4
                            actionCooldown = 0
                            
                        if (playersSelecteds[0][0].alive == False) and (playersSelecteds[0][1].alive == False) and (playersSelecteds[0][2].alive == True):
                            enemyList[1].attack(playersSelecteds[0][2])
                            currentFighter += 1
                            lastPlayer = 4
                            actionCooldown = 0
            elif enemyList[1].alive == False and lastPlayer != 2:
                currentFighter = 2

            elif enemyList[1].alive == False and lastPlayer != 3:
                currentFighter = 3

            elif enemyList[1].alive == False and lastPlayer != 5:
                currentFighter = 5
                
            else:
                currentFighter = 1
            
            #ATAQUE DO ALIADO 3 (JOGADOR 5)
            if playersSelecteds[0][2].alive == True:
                if currentFighter == 5 and lastPlayer != 5:
                    actionCooldown += 1
                    if actionCooldown >= actionWaitTime:
                        turn5()
                        #VERIFICAÇÃO DE AÇÃO
                        #ATAQUE
                        if (attack == True) and (target != None):
                            if target.alive != False:
                                playersSelecteds[0][2].attack(target)
                            currentFighter += 1
                            lastPlayer = 5
                            actionCooldown = 0
            elif playersSelecteds[0][2].alive == False and lastPlayer != 1:
                currentFighter = 1

            elif playersSelecteds[0][2].alive == False and lastPlayer != 2:
                currentFighter = 2

            elif playersSelecteds[0][2].alive == False and lastPlayer != 4:
                currentFighter = 4
                
            else:
                currentFighter = 3
                                    
            #REINICIALIZAÇÃO DA VEZ DOS PERSONAGENS
            if currentFighter > totalFighters:
                currentFighter = 1
                                                
            #SUBSTITUIÇÃO DO MOUSE PARA UMA ESPADA
            pg.mouse.set_visible(False)
            screenMatch.blit(swordImg, pos)

            #ATUALIZAR
            pg.display.update()

#INICIALIZAÇÃO DO JOGO
Game(screen, bg).mainMenu(screen, bg)