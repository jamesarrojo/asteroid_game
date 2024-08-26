import pygame
from constants import *
import player # we could do this like this `from player import Player`, so that...

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  clock = pygame.time.Clock()
  dt = 0
  playerInstance = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS) # ...we just do this like this `player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)`
  while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return
     screen.fill("black")
     playerInstance.draw(screen)
     playerInstance.update(dt)
     pygame.display.flip()
     dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()