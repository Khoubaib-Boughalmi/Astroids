from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

import pygame

def main():
    pygame.init()
    dt = 0
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = fps.tick(60) / 1000 # amount of time that has passed since last call in ms
        screen.fill(color=(0, 0, 0))
        for unit in updatable:
            unit.update(dt)
        for unit in drawable:
            unit.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
