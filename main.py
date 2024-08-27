import pygame
from constants import *
import player # we could do this like this `from player import Player`, so that...
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  clock = pygame.time.Clock()
  dt = 0
  playerInstance = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS) # ...we just do this like this `player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)`
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  updatable.add(playerInstance)
  drawable.add(playerInstance)
  
  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable

  asteroid_field = AsteroidField()
  while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return
        
     screen.fill("black")
     dt = clock.tick(60) / 1000

     for updatableObj in updatable:
        updatableObj.update(dt)
     for drawableObj in drawable:
        drawableObj.draw(screen)

     pygame.display.flip()

if __name__ == "__main__":
    main()