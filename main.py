from constants import *
from player import Player
import pygame

def main():
    pygame.init()
    dt = 0
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = fps.tick(60) / 1000 # amount of time that has passed since last call in ms
        screen.fill(color=(0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
