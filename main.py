import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

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

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # asteroid group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    # shots group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # instantiating player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    gamer = Player(x, y)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        log_state()
        screen.fill("black")
        
        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(gamer):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.split()

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
