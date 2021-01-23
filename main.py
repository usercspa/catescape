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

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

cat_width = 56

#gameloop
def game_loop():
    run = False

while not run:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      pygame.quit()

  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      x_change = -5
    if event.key == pygame.K_RIGHT:
      x_change = 5

  if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
     x_change = 0

  x += x_change

game_loop()

#cat position 
def cat(x,y):
  screen.blit(catimg, (x, y))

cat(x, y)

#background
def background():
  screen.blit(grass,(0,0))
  screen.blit(grass,(700,0))
  screen.fill((120,120,120))


background()


catimg = pygame.image.load("cat.gif")
grass = pygame.image.load("grass.png")
screen.blit(catimg,(400,470))


if x < 120 or x > 680-cat_width:
  run = True

clock = pygame.time.Clock()
clock.tick(100)
pygame.display.update()

myfont = pygame.font.SysFont("None", 100)
 render_text = myfont.render(“Cat crashed”,1,(255,255,255))