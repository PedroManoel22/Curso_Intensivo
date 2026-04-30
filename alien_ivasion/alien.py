import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota"""

    def __init__(self, ai_settings: Settings, screen: pygame.Surface):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load("Curso_Intensivo/alien_ivasion/images/teste.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superiro esquerda da tela

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)
