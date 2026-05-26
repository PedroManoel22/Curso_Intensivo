import os

import pygame
from pygame.sprite import Sprite
from settings import Settings


class Drops(Sprite):
    """Uma classe que representa uma única gota da chuva"""

    def __init__(self, ai_settings: Settings, screen: pygame.Surface):
        """Inicializa a gota e define sua posição inicial."""
        super(Drops, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        diretorio_atual = os.path.dirname(__file__)

        caminho_imagem = os.path.join(diretorio_atual, "image", "gota2.bmp")

        # Carrega a imagem da gota e define seu atributo rect
        self.image = pygame.image.load(caminho_imagem)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        # Inicia cada nova gota próximo à parte superior esquerda da tela

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da gota
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha a gota em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Devolve True se a gota estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienígena para a direita ou para a esquerda."""
        self.x += self.ai_settings.drop_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = int(self.x)
