from typing import Any

import pygame
from pygame.sprite import Group

import Curso_Intensivo.alien_ivasion.game_functions as gf
from Curso_Intensivo.alien_ivasion.button import Button
from Curso_Intensivo.alien_ivasion.game_stats import GameStats
from Curso_Intensivo.alien_ivasion.settings import Settings
from Curso_Intensivo.alien_ivasion.ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht, ai_settings.screen_height)
    )
    # Janela inteira do jogo
    pygame.display.set_caption("Alien Invasion")

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)

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
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button)


run_game()
