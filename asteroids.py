from constants import *
from circleshape import CircleShape
import random
import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x,y,radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    #separation_degrees = random.uniform(20, 50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    separation_degrees = [x for x in range(0, 360, 30)]
    for angle in separation_degrees:
      asteroid = Asteroid(self.position.x,self.position.y, new_radius)
      asteroid.velocity = self.velocity.rotate(angle) * 2

    # new_vector = self.velocity.rotate(separation_degrees)
    # new_vector2 = self.velocity.rotate(-separation_degrees)
    # asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    # asteroid_1.velocity = new_vector * 1.2
    # asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    # asteroid_2.velocity = new_vector2 * 1.2