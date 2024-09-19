import pygame
import sys
from player import Player
from asteroids import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

def main():
  pygame.init()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  Shot.containers = (shots, updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    for item in updatable:
      item.update(dt)
    for asteroid in asteroids:
      if(asteroid.check_collision(player)):
        sys.exit()
      for shot in shots:
        if(shot.check_collision(asteroid)):
          asteroid.split()
          shot.kill()

    for element in drawable:
      element.draw(screen)
    player.shot_timer -= dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()