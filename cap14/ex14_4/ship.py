from pathlib import Path

import pygame
from pygame.sprite import Sprite
from settings import Settings


class Ship(Sprite):
    def __init__(self, ai_settings: Settings, screen: pygame.Surface) -> None:
        super(Ship, self).__init__()
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings
        BASE_DIR = Path(__file__).parent
        image_path = BASE_DIR / "images" / "ship.bmp"

        # Carega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load(str(image_path))  # Carregando a imagem

        # Definindo um novo tamanho para a imagem
        novo_tamanho = (50, 50)

        # Mudando o tamanho da imagem: pygame.transform.scale recebe a superfície original e o novo tamanho
        self.image = pygame.transform.scale(self.image, novo_tamanho)

        self.rect = self.image.get_rect()  # Pegando o rect da imagem
        self.screen_rect = screen.get_rect()  # Pegando o rect da tela

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da espaçonave de acordo com as flags de movimento"""

        # Atualiza o valor do centro da espaçonave, e não do retâgulo ( lado direito ) e não deixa a espaçonave passar direto no lado direito
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # Atualiza o valor do centro da espaçonave, e não do retâgulo ( lado esquerdo ) e não deixa a espaçonave passar direto no lado esquerdo
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = int(self.center)
        self.rect.centery = int(self.y)

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.screen_rect.centerx
