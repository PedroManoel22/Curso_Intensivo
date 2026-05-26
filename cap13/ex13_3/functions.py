from __future__ import annotations

from typing import Any

import pygame
from drops import Drops
from pygame.sprite import Group
from settings import Settings


def get_number_drops_x(ai_settings: Settings, drop_width: int) -> int:
    """Determina o número de gotas que cabem em uma linha."""
    # Corrigido o erro de digitação 'widht' para 'width'
    available_space_x = ai_settings.screen_width - 2 * drop_width
    number_drops_x = available_space_x // (2 * drop_width)
    return number_drops_x


def get_number_rows(ai_settings: Settings, drop_height: int) -> int:
    """Determina o número de linhas de gotas que cabem na tela."""
    # Removida a dependência da 'ship_height' já que o foco são as gotas
    available_space_y = ai_settings.screen_height - (3 * drop_height)
    number_rows = available_space_y // (2 * drop_height)
    return number_rows


def create_star(
    ai_settings: Settings,
    screen: pygame.Surface,
    drops: Group[Any],
    drop_number: int,
    row_number: int,
):
    """Cria uma gota e a posiciona na grelha."""
    drop = Drops(ai_settings, screen)
    drop_width = drop.rect.width
    drop.x = drop_width + 2 * drop_width * drop_number
    drop.rect.x = drop.x
    drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
    drops.add(drop)


def create_fleet(ai_settings: Settings, screen: pygame.Surface, drops: Group[Any]):
    """Cria uma chuva."""
    # Criamos uma gota temporária apenas para medir as dimensões
    drop = Drops(ai_settings, screen)
    number_drops_x = get_number_drops_x(ai_settings, drop.rect.width)
    number_rows = get_number_rows(ai_settings, drop.rect.height)

    for row_number in range(number_rows):
        for drop_number in range(number_drops_x):
            create_star(ai_settings, screen, drops, drop_number, row_number)


def update_screen(
    ai_settings: Settings, screen: pygame.Surface, drops: "Group[Any]"
) -> None:
    """Atualiza as imagens na tela e alterna para a nova tela."""
    screen.fill(ai_settings.bg_color)
    drops.draw(screen)
    pygame.display.flip()


def check_fleet_edges(ai_settings: Settings, drops: Group[Any]):
    """Responde apropriadamente se alguma gota alcançou uma borda."""

    for drop in drops.sprites():
        if drop.check_edges():
            change_fleet_direction(ai_settings, drops)
            break


def change_fleet_direction(ai_settings: Settings, drops: Group[Any]):
    """Faz toda a frota descer e muda a sua direção."""
    for drop in drops.sprites():
        drop.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def update_drops(ai_settings: Settings, drops: Group[Any]):
    """
    Verifica se a chuva está em uma das bordas
    e então atualiza as posições de todas as gotas da chuva.
    """

    check_fleet_edges(ai_settings, drops)
    drops.update()
