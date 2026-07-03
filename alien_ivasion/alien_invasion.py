from typing import Any

import game_functions as gf
import pygame
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht, ai_settings.screen_height)
    )
    # Janela inteira do jogo
    pygame.display.set_caption("Alien Invasion")

    # Cria uma instância para armazenar dados estatísticos do jogo e cria painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    # # Cria um alienígena
    # alien = Alien(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets: Group[Any] = Group()

    aliens: Group[Any] = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(
            ai_settings, screen, ship, aliens, bullets, stats, sb, play_button
        )


run_game()
