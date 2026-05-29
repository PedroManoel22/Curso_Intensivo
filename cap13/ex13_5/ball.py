import random

import pygame
from pygame.sprite import Sprite
from settings import Settings


class Ball(Sprite):
    def __init__(self, screen: pygame.Surface, ai_settings: Settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Cria o rect da bola (vamos desenhar um círculo/retângulo vermelho)
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.screen_rect = screen.get_rect()

        # Posiciona a bola em um X aleatório no topo da tela
        self.reset_ball()

    def reset_ball(self):
        # Reposiciona a bola no topo com um X aleatório
        self.rect.top = 0
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.y = float(self.rect.y)

    def update(self):
        # Move a bola para baixo
        self.y += self.ai_settings.ball_speed
        self.rect.y = int(self.y)

    def draw(self):
        # Desenha uma bola vermelha na tela
        pygame.draw.ellipse(self.screen, (255, 0, 0), self.rect)
