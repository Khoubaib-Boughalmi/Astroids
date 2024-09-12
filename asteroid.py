from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), center=(self.position[0], self.position[1]), radius=self.radius, width=2)

    def update(self, dt):
        self.position[0] += ASTEROID_SPEED * dt
        self.position[1] += ASTEROID_SPEED * dt