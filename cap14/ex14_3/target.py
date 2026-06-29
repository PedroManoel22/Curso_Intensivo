from __future__ import annotations

import pygame
from settings import Settings


class Target:
    """Retângulo-alvo que se move verticalmente na borda direita."""

    def __init__(self, settings: "Settings", screen: pygame.Surface) -> None:
        self.screen = screen
        self.settings = settings
        self.color = settings.target_color

        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.target_width, settings.target_height)
        self.rect.midright = (self.screen_rect.right - 10, self.screen_rect.centery)

        # posição vertical precisa e direção (1 = desce, -1 = sobe)
        self.y = float(self.rect.y)
        self.direction = 1

    def update(self) -> None:
        """Move-se para cima e para baixo a velocidade constante; rebate nas bordas."""
        # ALTERADO: Mudamos target_speed para alien_speed_factor
        self.y += self.settings.alien_speed_factor * self.direction
        self.rect.y = int(self.y)

        # Rebate nas bordas superior/inferior
        if self.y <= 0:
            self.y = 0.0
            self.direction = 1
        elif self.y + self.rect.height >= self.screen_rect.bottom:
            self.y = float(self.screen_rect.bottom - self.rect.height)
            self.direction = -1

        self.rect.y = int(self.y)

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)
