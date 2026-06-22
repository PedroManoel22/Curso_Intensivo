from __future__ import annotations

import pygame


class Button:
    """Um botão simples."""

    def __init__(self, screen: pygame.Surface, msg: str) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensões/propriedades
        self.width, self.height = 240, 60
        self.button_color = (70, 150, 90)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 42)

        # Construção do retângulo do botão
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
