import pygame
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship


class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave"""

    def __init__(self, ai_settings: Settings, screen: Surface, ship: Ship):
        """Cria um objeto para o projétil na posição atual da
        espaçonave."""

        super(Bullet, self).__init__()
        self.screen = screen

        # Cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta

        self.image: Surface = pygame.Surface(
            (ai_settings.bullet_width, ai_settings.bullet_height)
        )
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )

        self.rect.midleft = ship.rect.midleft

        # Armazena a posição do projétil como um valor decimal
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projétil para a direita na tela."""
        # Atualiza a posição decimal do projétil

        self.x += self.speed_factor

        # Atualiza a posição de rect

        self.rect.x = int(self.x)

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
