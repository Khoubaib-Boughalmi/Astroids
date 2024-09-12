from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), center=(self.position[0], self.position[1]), radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_angle = random.randint(20, 51)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_jr1 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        asteroid_jr2 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        
        asteroid_jr1.velocity = self.velocity.rotate(new_angle) * 1.2
        asteroid_jr2.velocity = self.velocity.rotate(-new_angle) * 1.2
