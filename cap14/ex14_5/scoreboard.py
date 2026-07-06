from typing import Any

import pygame
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship


class Scoreboard:
    """Uma classe para mostrar informações sobre pontuação."""

    def __init__(
        self, ai_settings: Settings, screen: pygame.Surface, stats: GameStats
    ) -> None:
        """Inicializa os atributos da pontuação"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (255, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        # Refatorado: Substitui as quatro chamadas diretas por um único método conciso
        self.prep_images()

    def prep_images(self) -> None:
        """Prepara todas as imagens iniciais e atualizadas do painel de pontuação."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self) -> None:
        """Transforma a pontuação em uma imagem renderizada."""
        # Nota: Removi a linha redundante que quebrava a formatação com vírgulas
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self) -> None:
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self) -> None:
        """Transforma a pontuação máxima em uma imagem renderizada."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color
        )

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self) -> None:
        """Transforma o nível em uma imagem renderizada."""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.ai_settings.bg_color
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self) -> None:
        """Mostra quantas espaçonaves restam."""
        self.ships: Group[Any] = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
