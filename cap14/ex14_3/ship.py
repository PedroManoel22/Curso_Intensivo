from __future__ import annotations

import pygame
from settings import Settings


class Ship:
    """Nave controlada pelo jogador (move verticalmente)."""

    COLOR = (230, 230, 255)

    def __init__(self, settings: Settings, screen: pygame.Surface) -> None:
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Um retângulo simples para a nave
        self.width, self.height = 50, 30
        self.color = self.COLOR
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.center_ship()

        # Flags de movimento
        self.moving_up = False
        self.moving_down = False

        # Posição vertical precisa
        self.y = float(self.rect.y)

    def center_ship(self) -> None:
        """Posiciona a nave no lado esquerdo, centrada verticalmente."""
        self.rect.midleft = (20, self.screen_rect.centery)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Atualiza a posição vertical com base nas flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = int(self.y)

    def blitme(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)
