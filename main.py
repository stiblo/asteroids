import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    clock_object = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw_object in drawable:
            draw_object.draw(screen)
        pygame.display.flip()
        dt = clock_object.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()