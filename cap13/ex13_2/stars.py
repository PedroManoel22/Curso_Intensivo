import pygame
from pygame.sprite import Sprite
from settings import Settings


class Stars(Sprite):
    """Uma classe que representa um único alienígena da frota"""

    def __init__(self, ai_settings: Settings, screen: pygame.Surface):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Stars, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da estrela e define seu atributo rect
        self.image = pygame.image.load("Curso_Intensivo/cap13/ex13_1/image/stars.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Inicia cada nova estrela próximo à parte superior esquerda da tela

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da estrela
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha a estrela em sua posição atual."""
        self.screen.blit(self.image, self.rect)
