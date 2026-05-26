from typing import Any

import game_functions as gf
import pygame
from pygame.sprite import Group
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

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # # Cria um alienígena
    # alien = Alien(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets: Group[Any] = Group()

    aliens: Group[Any] = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
