import pygame
import circleshape # from circleshape import CircleShape
# from constants import *

class Player(circleshape.CircleShape):
  def __init__(self, x, y, radius): # def __init__(self, x, y):
    super().__init__(x, y, radius) # super().__init__(x, y, PLAYER_RADIUS)
    self.position = pygame.Vector2(x, y)
    self.rotation = 0
    # self.radius = PLAYER_RADIUS

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)
    # return super().draw(screen) # this is not needed
