import pygame
from constants import *

def main():
  print("Starting asteroids!")
  pygame.init()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0,0,0))
    pygame.display.flip()
if __name__ == "__main__":
    main()

