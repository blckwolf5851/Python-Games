import mergeUp
from math import log
import mergeLeft
import mergeRight
import mergeDown
import pygame
import random
import time
import math
WIDTH = 400
HEIGHT = 500
frame = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('2048')

blockSize = 100
black = (0,0,0)
white = (255,255,255)
pink=(255,0,255)
lightBlue = (0,255,255)
yellow = (255,255,0)
brown = (82, 55, 26)
boxColor = (207, 196, 162)
pygame.init()
init = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
font = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 30)
box = WIDTH/len(init)



def message(msg,color,xy):
    text = font2.render(msg,True,color)
    frame.blit(text,list(xy))
def gameOver(line):
    failCount = 0
    for row in range(len(line)):
        for colum in range(len(line[1])-1):
            if line[row][colum] != line[row][colum+1] and 0 not in line[row]:
                failCount +=1
    for colum in range(len(line[1])):
        for row in range(len(line)-1):
            if line[row][colum] != line[row+1][colum] and 0 not in line[row]:
                failCount+=1
    if failCount == (len(line)*(len(line[1])-1)+(len(line)-1)*len(line[1])): # total number of rows all have no 0 and doesn't equal to each other, game over
        return 1
def spawn(line):
    num = random.randrange(2,5,2) #pick a random number to display (either 2 or 4)
    zeroIndex = [] #all the indexs that is has value of zero, later chose from those 0 index to put new value
    for row in range(len(line)): # append lists of indexs to zeroIndex
        for colum in range(len(line[row])):
            if line[row][colum] == 0:
                zeroIndex.append([row,colum])
    if len(zeroIndex)>0:
        for i in range(1,2): # pick random index from zeroIndex
            randomIndex = random.randrange(0,len(zeroIndex))
            pickIndex = zeroIndex[randomIndex]
            row = pickIndex[0]
            colum = pickIndex[1]
            line[row][colum] = num
    zeroIndex = [] # reset zeroIndex
def drawgrid(score):
    frame.fill(brown)
    for x in range(0,len(init)):
        for y in range(0,len(init[0])):
            if init[x][y] == 0:
                color = (115, 74, 30)
            else:
                color = (207, 196, 255-(23*(log(init[x][y])/log(2))))
            pygame.draw.rect(frame, color, (y*box, x*box, 95,95))
            if init[x][y] > 0:
                label = font.render(str(init[x][y]), True ,brown)
                frame.blit(label, (y*box + 32, x*box + 32))
                message('Score: '+str(score),boxColor ,[WIDTH/2-50,440])
            else:
                label = font.render(' ', True ,brown)
                frame.blit(label, (y*box + 32, x*box + 32))
    pygame.display.update()
def gameloop():
    global init
    score = 0
    init = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    init[random.randrange(0,4)][random.randrange(0,4)] = 2

    gameExit = False
    gamedone = False
    while not gameExit:
        while gamedone == True:
            time.sleep(2)
            frame.fill(brown)
            message('GameOver. c to continue, q to quit', boxColor,[WIDTH/2-180,HEIGHT/2])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gamedone = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mergeLeft.mergeLeft(init)
                    spawn(init)
                    score += 1
                elif event.key == pygame.K_RIGHT:
                    mergeRight.mergeRight(init)
                    spawn(init)
                    score += 1
                elif event.key == pygame.K_UP:
                    mergeUp.mergeUp(init)
                    spawn(init)
                    score += 1
                elif event.key == pygame.K_DOWN:
                    mergeDown.mergeDown(init)
                    spawn(init)
                    score += 1
            if event.type == pygame.QUIT:
                gameExit=True
        if gameOver(init)==1:
            gamedone=True

        drawgrid(score)

        pygame.display.update()


gameloop()
