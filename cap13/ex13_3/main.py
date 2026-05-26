# 13.1 – Estrelas: Encontre uma imagem de uma estrela. Faça uma grade de estrelas
# aparecer na tela.


import sys
from typing import Any

import pygame
from functions import create_fleet, update_drops, update_screen
from pygame.sprite import Group
from settings import Settings


def run_game(title: str = "Gotas de Chuva"):
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    drops: Group[Any] = Group()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    # Cria a frota de estrelas
    create_fleet(ai_settings, screen, drops)
    # Janela inteira do jogo
    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    # Inicia o laço principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update_screen(ai_settings, screen, drops)
        update_drops(ai_settings, drops)

        clock.tick(30)  # limita para 30 fps


run_game()
