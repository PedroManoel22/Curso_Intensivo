from __future__ import annotations

from typing import Any

import game_functions as gf
import pygame
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from target import Target


def run_game() -> None:
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Treino de Tiro ao Alvo — Ex 14.2")

    # Objetos principais
    stats = GameStats(settings)
    play_button = Button(screen, "Play")
    ship = Ship(settings, screen)
    bullets: Group[Any] = Group()
    target = Target(settings, screen)

    clock = pygame.time.Clock()

    # Loop principal
    while True:
        gf.check_events(settings, screen, stats, play_button, ship, bullets, target)
        gf.update_all(settings, screen, stats, ship, bullets, target)
        gf.update_screen(settings, screen, stats, play_button, ship, bullets, target)
        clock.tick(60)


if __name__ == "__main__":
    run_game()
