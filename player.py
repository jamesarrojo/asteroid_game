import pygame
import circleshape # from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
  def __init__(self, x, y, radius): # def __init__(self, x, y):
    super().__init__(x, y, radius) # super().__init__(x, y, PLAYER_RADIUS)
    self.position = pygame.Vector2(x, y)
    self.rotation = 0
    self.rate_limit_timer = 0
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
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
  def update(self, dt):
    self.rate_limit_timer -= dt
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      self.shoot()

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.rate_limit_timer > 0:
      return
    self.rate_limit_timer = PLAYER_SHOOT_COOLDOWN
    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    # my solution
    # shot.velocity = pygame.Vector2(0, 1)
    # shot.velocity = shot.velocity.rotate(self.rotation)
    # shot.velocity *= PLAYER_SHOOT_SPEED # i think no need to do the *= since shoot() gets called every time we hit space
    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED