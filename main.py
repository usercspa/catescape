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
opening = pygame.image.load("opening.png")

#cat position 
def cat(x,y):
  screen.blit(catimg, (x, y))



#obstacles
def obstacles(obx, oby, obw, obh, color):
    pygame.draw.rect(screen, color, [obx, oby, obw, obh])    

#caught
def caught():
    display_message('You got caught')


#score
def obstacle_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    screen.blit(text,(350,50))

#start screen
def game_opening():
    screen.blit(opening,(0,0))
    pygame.display.update()
    time.sleep(1)    

#end screen
def display_message(content):
    pygame.time.delay(500)
    screen.fill(black)
    font = pygame.font.SysFont(None, 100)
    text = font.render(("You got caught"), True, white)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, (WIDTH - text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)

#game loop    
def game_loop():

    game_opening()


    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)

    x_change = 0

    ob_startx = random.randrange(0, WIDTH)
    ob_starty = -600
    ob_speed = 7
    ob_width = 100
    ob_height = 100

    obCount = 1

    dodged = 0

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

        obstacles(ob_startx, ob_starty, ob_width, ob_height, white)
        ob_starty += ob_speed
        cat(x,y)
        obstacle_dodged(dodged)

        if x > WIDTH - cat_width or x < 0:
            caught()

        if ob_starty > HEIGHT:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0,WIDTH)
            dodged += 1
            ob_speed += 1
            ob_width += (dodged * 1.2)


        if y < ob_starty+ob_height:
            
            if x > ob_startx and x < ob_startx + ob_width or x+cat_width > ob_startx and x + cat_width < ob_startx+ob_width:
                
          
              caught()

        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
