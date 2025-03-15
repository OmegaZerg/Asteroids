import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        pygame.display.flip()
        #limit the framerate to 60 FPS
        dt = fps_clock.tick(60)/1000

if __name__ == "__main__":
    main()