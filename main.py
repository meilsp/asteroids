import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    
    # delta time setup
    clock = pygame.time.Clock()
    dt = 0

    # drawing screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # instantiating player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    gamer = Player(x, y)

    # game loop
    while True:
        log_state()
        screen.fill("black")
        gamer.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
