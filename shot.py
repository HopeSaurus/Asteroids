import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
  def __init__(self, x, y, rotation):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = SHOT_SPEED
    self.forward = pygame.Vector2(0, 1).rotate(rotation)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

  def update(self, dt):
    self.position += self.forward * self.velocity * dt