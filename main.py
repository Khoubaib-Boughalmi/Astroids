from constants import *
import pygame

def main():
    pygame.init()
    dt = 0
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=0)
        pygame.display.flip()
        dt = fps.tick(60) / 1000 # amount of time that has passed since last call in ms


if __name__ == "__main__":
    main()
