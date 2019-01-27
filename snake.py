import pygame
import random
import time
WIDTH = 420
HEIGHT=550
frame = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake Game')

blockSize = 10
black = (0,0,0)
white = (255,255,255)
pink=(255,0,255)
lightBlue = (0,255,255)
yellow = (255,255,0)
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont(None, 30)
def message(msg,color):
    text = font.render(msg,True,color)
    frame.blit(text,[WIDTH/2-160,HEIGHT/2])

def drawSnake(snakeBody,blockSize):
    for body in snakeBody:
        pygame.draw.rect(frame,white, [body[0],body[1],blockSize,blockSize])
def drawSnake2(snakeBody,blockSize):
    for body in snakeBody:
        pygame.draw.rect(frame, pink, [body[0],body[1],blockSize,blockSize])

#draw snake function
def gameloop():
    xpos=WIDTH-20
    ypos=HEIGHT-20
    xpos2=20
    ypos2=20
    accx=0
    accy = 0
    accx2 = 0
    accy2 = 0
    snakeBody=[]
    gameExit = False
    gameOver = False
    randX = random.randrange(0,410,10)
    randY = random.randrange(0,540,10)
    snakeBody2=[]
    snakeLength = 1
    snakeLength2 = 1
    while not gameExit:
        while gameOver == True:
            frame.fill(black)
            message('GameOver. c to continue, q to quit', white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        gameExit=True
                    if event.key == pygame.K_c:
                        gameloop()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    accx = -10
                    accy = 0
                elif event.key == pygame.K_RIGHT:
                    accx=10
                    accy = 0
                elif event.key == pygame.K_UP:
                    accy=-10
                    accx=0
                elif event.key == pygame.K_DOWN:
                    accy=10
                    accx=0
                if event.key == pygame.K_a:
                    accx2 = -10
                    accy2 = 0
                elif event.key == pygame.K_d:
                    accx2=10
                    accy2 = 0
                elif event.key == pygame.K_w:
                    accy2=-10
                    accx2=0
                elif event.key == pygame.K_s:
                    accy2=10
                    accx2=0
                if event.key == pygame.K_SPACE and len(snakeBody)>2:
                    if accx > 0 :
                        xpos += 20
                    elif accx < 0:
                        xpos -= 20
                    elif accy > 0:
                        ypos += 20
                    elif accy < 0 :
                        ypos -= 20
                    #del snakeBody[0]
                    #snakeBody.pop(1)
                if event.key == pygame.K_f and len(snakeBody2)>2:
                    if accx2 > 0 :
                        xpos2 += 20
                    elif accx2 < 0:
                        xpos2 -= 20
                    elif accy2 > 0:
                        ypos2 += 20
                    elif accy2 < 0 :
                        ypos2 -= 20
                    #del snakeBody2[0]
                    #snakeBody2.pop(1)

            if event.type == pygame.QUIT:
                gameExit=True
        frame.fill(black)
        pygame.draw.rect(frame, (0,255,255), [randX,randY,blockSize,blockSize])

        xpos += accx
        ypos += accy
        xpos2 += accx2
        ypos2 += accy2

        snakeHead=[]
        snakeHead2=[]
        snakeHead.append(xpos)
        snakeHead.append(ypos)
        snakeHead2.append(xpos2)
        snakeHead2.append(ypos2)
        snakeBody.append(snakeHead)
        snakeBody2.append(snakeHead2)

        if len(snakeBody) > snakeLength:
            del snakeBody[0]
        if len(snakeBody2) > snakeLength2:
            del snakeBody2[0]
        drawSnake(snakeBody,blockSize)
        drawSnake2(snakeBody2,blockSize)
        pygame.display.update()
        if xpos == randX and ypos == randY:
            randX = random.randrange(0,410,10)
            randY = random.randrange(0,540,10)
            snakeLength += 1
        if xpos2 == randX and ypos2 == randY:
            randX = random.randrange(0,410,10)
            randY = random.randrange(0,540,10)
            snakeLength2 += 1


        for ind in snakeBody[:-1]:
            if ind == snakeHead:
               gameOver = True
        for ind in snakeBody2[:-1]:
            if ind == snakeHead2:
               gameOver = True
        if snakeHead in snakeBody2:
            message('Pink Snake Wins',pink)
            pygame.display.update()
            time.sleep(2)
            gameOver = True
        elif snakeHead2 in snakeBody:
            message('White Snake Wins',white)
            pygame.display.update()
            time.sleep(2)
            gameOver = True
        if xpos < 0 or xpos > 420 or ypos < 0 or ypos > 550 or xpos2 < 0 or xpos2 > 420 or ypos2 < 0 or ypos2 > 550:
            gameOver = True

        clock.tick(15+(len(snakeBody)+len(snakeBody2))*0.1)

    pygame.quit()
    quit()
gameloop()
