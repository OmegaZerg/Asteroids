from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.color = (255, 255, 255)
        self.shot_cooldown = 0
        self.shot_delay = 0.4

    #Define player
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #Draw player
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), width=2)
        
    #Player Movement
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)   

        #Reduce cooldown timer if it's active
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

    #player shots
    def shoot(self, bullets):
        if self.shot_cooldown <= 0:
            #create new shot
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

            #Set shot velocity
            shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED

            #Add to bullets group
            bullets.add(new_shot)

            #Reset cooldown timer
            self.shot_cooldown = self.shot_delay
