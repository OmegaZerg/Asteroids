import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    dt = 0

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(000)
        player.draw(screen)
        
        pygame.display.flip()
        
        #limit the framerate to 60 FPS
        dt = fps_clock.tick(60)/1000

    

if __name__ == "__main__":
    main()