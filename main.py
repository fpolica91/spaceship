import pygame
import math
from spaceship import Spaceship
from bullet import Bullet
import sys






  

SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

background = pygame.image.load("images/space.jpg")
background_rect =  background.get_rect()
bgx2 = background.get_height()
bgx = 0

pygame.display.set_caption('Circles')
fps = pygame.time.Clock()
paused = False









    




spaceship = Spaceship(x=283, y=363, screen=screen)

class Game:
  def __init__(self, spaceship):
    self.SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
    self.spaceship = spaceship

  def render(self):
    screen.fill(BLACK)
    self.spaceship.draw(screen)
    pygame.display.update()
    fps.tick(60)
    pygame.display.flip()


game = Game(spaceship=spaceship)









bullets = []
pos = (250, 250)
run = True

while run:
 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          ship = game.spaceship
          bullets.append(Bullet(ship.x, ship.y, spaceship=ship))
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
              spaceship.up()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
              spaceship.down()
        if event.type == 769:
          if pygame.key.name(event.key) == "right":
            
            spaceship.right()
        if event.type == 768:
          if pygame.key.name(event.key) == "left":
            spaceship.left()
    for bullet in bullets[:]:
      bullet.update()
      if not screen.get_rect().collidepoint(bullet.pos):
        bullets.remove(bullet)
      
    
    bgx2 -= 1

    if bgx < background.get_height() * -1:
      bgx = background.get_height()

    if bgx2 < background.get_height() * -1:
      bgx2 = background.get_height()

    

      
    
  
    screen.blit(background, (0, bgx))
    screen.blit(background, (0, bgx2))
    # pygame.display.update()
    
    for bullet in bullets[:]:
      bullet.draw(screen)
    
    spaceship.draw(screen)
    pygame.display.update()
c
       
            
            

    # if not paused:
    #     game.render()
