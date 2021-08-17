import pygame
from pygame.locals import *
import random
import math
from calculatedistance import getdistance
pygame.init()

file = open(r"C:\Users\Dev Mehra\Documents\Python Projects\Pythonl\reinforcementlearning\SnakeRL\snakedata.csv",'a')
file.write('foodx,foody,snakex,snakey,reward,previousdirection,currentdirection\n')
#foodx,foody,snakex,snakey,previousdirection,currentdirection
previousdirection = ""
currentdirection = ""
reward = 0





def Game():
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Snake")

    white = (255,255,255)
    black = (0,0,0)
    green = (0,255,0)
    red = (255,0,0)
    foodx = ((random.randint(0,600)) // 10) * 10
    foody = ((random.randint(0,600)) // 10) * 10

    snakex = ((random.randint(0,600)) // 10) * 10
    snakey = ((random.randint(0,600)) // 10) * 10

    up = 0 
    down = 0
    left = 0
    right = 0
    clock = pygame.time.Clock()
    body = [[snakex,snakey]]

    speed = 10
    matchedx = 0
    previousdirection = 0
    currentdirection = ""

    previousdistancefromfood = 0
    currentdistancefromfood = 0
    while True:

        pygame.display.update()
        screen.fill(black)
        length = len(body)
        clock.tick(speed)
        body.insert(0,[snakex,snakey])
        body.pop()
        previousdistancefromfood = getdistance(snakex,snakey,foodx,foody)
        
        if left == 1:
            previousdirection = 0
        if right == 1:
            previousdirection = 1

        if up == 1:
            previousdirection = 2
        if down == 1:
            previousdirection = 3

        if matchedx == 0:
            if foodx == snakex:
                    left = 0 
                    right = 0
                    print(foodx,snakex)
                    matchedx = 1

            elif foodx < snakex and right == 0:
                
                    print("left")
                    left = 1
                    right = 0
                    # up = 0
                    # down = 0
                

            elif foodx > snakex and left == 0:

                    print("right")
                    right = 1
                    left = 0
                    # up = 0
                    # down = 0
        

        else:
            if foody == snakey:
                up = 0
                down = 0
                print(foody,snakey)
                matchedx = 0

            elif foody < snakey and down == 0:
                print("up")
                up = 1
                down = 0
                left = 0
                right = 0

            elif foody > snakey and up == 0:
                print("Down")
                down = 1
                up = 0
                left = 0
                right = 0

        # elif foody+10 < snakey:
        #     up = 1
        # elif foody+10 > snakey:
        #     down = 1



        if left == 1:
            snakex -= 10
            currentdirection = "left"
        if right == 1:
            snakex += 10
            currentdirection = "right"


        if up == 1:
            snakey -= 10
            currentdirection = "up"
        if down == 1:
            snakey += 10
            currentdirection = "down"
        

        if snakey<0:
            snakey = 590
        if snakey>600:
            snakey = 0
        if snakex<0:
            snakex = 590
        if snakex>600:
            snakex = 0
        
        
        currentdistancefromfood = getdistance(snakex,snakey,foodx,foody)


        if (currentdistancefromfood<previousdistancefromfood):
            reward = 1
        else:
            reward = -1


        if [snakex,snakey] in body[1:]:
            reward = 0
            #file.close()
            #exit()
            break




        if snakex == foodx and snakey == foody:
            #print("food eaten")
            foodx = ((random.randint(0,600)) // 10) * 10
            foody = ((random.randint(0,600)) // 10) * 10
            body.append([snakex,snakey])
            speed = speed+10
            reward = 100
            
            
        
        for segment in body:
            pygame.draw.rect(screen,green,segment+[10,10])
        
        # if body[0] in body[1:]:
        #     reward = 0
        #     exit()

        pygame.draw.rect(screen,red,(foodx,foody,10,10))

        
        writtenstring = str(foodx)+","+str(foody)+","+str(snakex)+","+str(snakey)+","+str(reward)+","+str(previousdirection)+","+str(currentdirection)+"\n"
        file.write(writtenstring)

        for event in pygame.event.get():
            if event.type == QUIT:
                file.close()
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_DOWN and up == 0:
                    #snakey += 10
                    down = 1
                    up = 0
                    left = 0
                    right = 0
                if event.key == K_UP and down == 0:
                    #snakey -= 10
                    up = 1
                    down = 0
                    left = 0
                    right = 0
                if event.key == K_LEFT and right == 0:
                    #snakex -= 10
                    left = 1
                    up = 0
                    down = 0
                    right = 0
                if event.key == K_RIGHT and left == 0:
                    #snakex += 10
                    right = 1
                    up = 0
                    down = 0
                    left = 0


for i in range(5):
    Game()


file.close()