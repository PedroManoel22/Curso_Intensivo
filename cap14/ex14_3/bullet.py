from __future__ import annotations

import pygame
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship


class Bullet(Sprite):
    """Projétil disparado pela nave (move para a direita)."""

    def __init__(self, settings: Settings, screen: pygame.Surface, ship: Ship):
        super().__init__()
        self.screen = screen
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        # Origina na borda direita da nave, centrado verticalmente na nave
        self.rect.midleft = ship.rect.midright

        # posição x precisa
        self.x = float(self.rect.x)

    def update(self) -> None:
        # Move o projétil para a direita
        self.x += self.speed
        self.rect.x = int(self.x)

    def draw_bullet(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)
