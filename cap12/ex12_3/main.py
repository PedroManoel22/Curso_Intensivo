# 12.3 – Foguete: Crie um jogo que comece com um foguete no centro da tela.
# Permita que o jogador mova o foguete para cima, para baixo, para a direita e
# para a esquerda usando as quatro teclas de direção. Garanta que o foguete não
# se desloque para além de qualquer borda da tela.

import game_functions as gf
import pygame
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

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
