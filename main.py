import pygame
from constants import *
import player # we could do this like this `from player import Player`, so that...
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  
  dt = 0
  playerInstance = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS) # ...we just do this like this `player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)`
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  updatable.add(playerInstance)
  drawable.add(playerInstance)
  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  Shot.containers = shots

  asteroid_field = AsteroidField()
  
  while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return
        
     for updatableObj in updatable:
        updatableObj.update(dt)

     for asteroid in asteroids:
        if playerInstance.have_collided(asteroid) == True:
           print('Game over!')
           sys.exit()

     screen.fill("black")

     for drawableObj in drawable:
        drawableObj.draw(screen)
     for shot in shots:
        shot.draw(screen)
        shot.update(dt)

     pygame.display.flip()

     dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()