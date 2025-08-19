import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x=x, y=y, radius=SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color='white',
                           center=self.position,
                           radius=self.radius,
                           width=2)

    def update(self, dt):
        self.position += self.velocity * dt
