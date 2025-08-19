import pygame
import random

from circleshape import CircleShape

from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x=x, y=y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color='white',
                           center=self.position,
                           radius=self.radius,
                           width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        # v1 = self.velocity * random_angle
        v1 = self.velocity.rotate(random_angle)
        # v2 = self.velocity * -random_angle
        v2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(x=self.position[0], y=self.position[1], radius=new_radius)
        asteroid_2 = Asteroid(x=self.position[0], y=self.position[1], radius=new_radius)

        asteroid_1.velocity = v1 * 1.2
        asteroid_2.velocity = v2 * 1.2

