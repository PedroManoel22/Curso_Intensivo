import pygame


class Ship:
    def __init__(self, screen: pygame.Surface) -> None:
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen

        # Carega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load(
            "Curso_Intensivo/alien_ivasion/images/ship.bmp"
        )  # Carregando a imagem

        # mudar tamanho da imagem
        novo_tamanho = (50, 50)

        # pygame.transform.scale recebe a superfície original e o novo tamanho
        self.image = pygame.transform.scale(self.image, novo_tamanho)

        self.rect = self.image.get_rect()  # Pegando o rect da imagem
        self.screen_rect = screen.get_rect()  # Pegando o rect da tela

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
