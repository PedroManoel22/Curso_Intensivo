from __future__ import annotations

from random import randint
from typing import Any

import pygame
from pygame.sprite import Group
from settings import Settings
from stars import Stars


def get_number_stars_x(ai_settings: Settings, star_width: int) -> int:
    """Determina o número de estrelas que cabem em uma linha."""
    # Corrigido o erro de digitação 'widht' para 'width'
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = available_space_x // (2 * star_width)
    return number_stars_x


def get_number_rows(ai_settings: Settings, star_height: int) -> int:
    """Determina o número de linhas de estrelas que cabem na tela."""
    # Removida a dependência da 'ship_height' já que o foco são as estrelas
    available_space_y = ai_settings.screen_height - (3 * star_height)
    number_rows = available_space_y // (2 * star_height)
    return number_rows


def create_star(
    ai_settings: Settings,
    screen: pygame.Surface,
    stars: Group[Any],
    star_number: int,
    row_number: int,
):
    """Cria uma estrela com um posicionamento levemente aleatório."""
    star = Stars(ai_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height

    # Cálculo da posição base (grelha fixa)
    base_x = star_width + 2 * star_width * star_number
    base_y = star_height + 2 * star_height * row_number

    # Adicionando a aleatoriedade sugerida no exercício
    random_offset_x = randint(-10, 10)
    random_offset_y = randint(-10, 10)

    # Aplica a posição final com o deslocamento
    star.rect.x = base_x + random_offset_x
    star.rect.y = base_y + random_offset_y

    stars.add(star)


def create_fleet(ai_settings: Settings, screen: pygame.Surface, stars: Group[Any]):
    """Cria uma frota completa de estrelas."""
    # Criamos uma estrela temporária apenas para medir as dimensões
    star = Stars(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)


def update_screen(ai_settings: Settings, screen: pygame.Surface, stars: "Group[Any]"):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()
