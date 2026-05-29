import pygame
from settings import Settings


class Character:
    def __init__(self, screen: pygame.Surface, ai_settings: Settings):
        self.screen = screen
        self.ai_settings = ai_settings

        try:
            self.image = pygame.image.load(
                "Curso_Intensivo/cap13/ex13_5/image/personagem2.html"
            )
            self.rect = self.image.get_rect()
        except pygame.error:
            self.image = None
            self.rect = pygame.Rect(0, 0, 80, 30)

        self.screen_rect = screen.get_rect()

        # Inicia o personagem na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        # Guarda um valor decimal para o centro do personagem
        self.center = float(self.rect.centerx)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza o centro do personagem com base nas flags e nos limites da tela
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.character_speed

        # Atualiza o objeto rect a partir de self.center
        self.rect.centerx = int(self.center)

    def draw(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, (0, 0, 255), self.rect)
