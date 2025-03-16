import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group() # holds objects that need to be updated each frame
    drawable = pygame.sprite.Group() # holds objects that need to be drawn each frame
    asteroids = pygame.sprite.Group() # holds the asteroid objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # clear screen before drawing
        screen.fill((0, 0, 0)) # RGB
        
        # Update and draw
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        
        # Check for collisions
        for obj in asteroids:
            if player.is_collision(obj):
                sys.exit("Game over man!")

        pygame.display.flip()
        
        #limit the framerate to 60 FPS
        dt = fps_clock.tick(60)/1000

    

if __name__ == "__main__":
    main()