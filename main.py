#install packages
import pygame
import time
import random

#initialize
pygame.init()

#screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat Escape")
clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (123,123,123)

cat_width = 56

#load images
catimg = pygame.image.load("cat.gif")
grass = pygame.image.load("grass.png")
human = pygame.image.load("human.png")

#cat position 
def cat(x,y):
  screen.blit(catimg, (x, y))

#text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()  

#message
def message_display(text):
    largeText = pygame.font.Font('None',115)
    TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    screen.blit(TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#caught
def caught():
    message_display('You got caught')
    
def game_loop():
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)

    x_change = 0

    human_startx = random.randrange(0, WIDTH)
    human_starty = -600
    human_speed = 7
    human_width = 100
    human_height = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(grey)

        human(human_startx, human_starty, human_width, human_height)
        human_starty += human_speed
        cat(x,y)

        if x > WIDTH - cat_width or x < 0:
            caught()

        if human_starty > HEIGHT:
            human_starty = 0 - human_height
            human_startx = random.randrange(0,WIDTH)


        if y < human_starty+human_height:
            print('y crossover')

            if x > human_startx and x < human_startx + human_width or x+cat_width > human_startx and x + cat_width < human_startx+human_width:
                print('x crossover')
                caught()

        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
