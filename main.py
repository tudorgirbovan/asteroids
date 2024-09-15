# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(window,(0,0,0))
        pygame.display.flip()
        
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   return

if __name__ == "__main__":
    main()
