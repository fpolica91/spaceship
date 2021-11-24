import pygame
import math 

class Bullet:
  def __init__(self, x ,y, spaceship):
    self.pos = (x, y)
    mx, my = pygame.mouse.get_pos()
    if my <= spaceship.y:
      self.dir = (mx - x, my - y)
    else:
      self.dir = (28, -295)
    
    length = math.hypot(*self.dir)

    if length == 0.0:
      self.dir = (0, -1)
    else:
      self.dir =  (self.dir[0]/length, self.dir[1]/length)
    
    angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
    self.bullet = pygame.Surface((10, 4)).convert_alpha()
    self.bullet.fill((255, 255, 255))
    self.bullet = pygame.transform.rotate(self.bullet, angle)
    self.speed = 2

  def update(self):
    self.pos = (self.pos[0] + self.dir[0] * self.speed, 
                  self.pos[1] + self.dir[1] * self.speed)
      
  
  def draw(self, screen):
    bullet_rect = self.bullet.get_rect(center = self.pos)
    screen.blit(self.bullet, bullet_rect)



    