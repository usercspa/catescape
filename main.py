#install packages
import pygame

#initialize
pygame.init()

#screen
WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Cat Escape")



#gameloop
def game_loop():
    run = False

while not run:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      pygame.quit()

game_loop()

#cat position 
def cat(x,y):
  screen.blit(catimg, (x, y))

cat(x, y)

screen.fill((120,120,120))
catimg = pygame.image.load("cat.gif")
screen.blit(catimg,(400,470))
pygame.display.update()

if event.type == pygame.KEYDOWN:
  if event.key == pygame.K_LEFT:
    x_change = -5
  if event.key == pygame.K_RIGHT:
    x_change = 5