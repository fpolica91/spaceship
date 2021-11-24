import pygame
SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)

class Spaceship:
  def __init__(self, x, y, screen):
    self.x = x
    self.y = y
    self.image = pygame.image.load("images/ship3.png").convert_alpha()
    self.screen = screen

  def draw(self, screen):
    image = pygame.transform.scale(self.image, (75, 75))
    image.set_colorkey((0,0,0))
    screen.blit(image, (self.x, self.y))
  def up(self):
    self.y -= 10
  def down(self):
    self.y += 10
  def right(self):
    self.x += 10
  def left(self):
    self.x -= 10
  
  






   
