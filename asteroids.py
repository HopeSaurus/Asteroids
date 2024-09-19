from constants import *
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x,y,radius)
    self.velocity = ASTEROID_VELOCITY

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    asteroid_1 = Asteroid(self.position.x, self.position.y)
