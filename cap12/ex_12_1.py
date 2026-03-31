# 12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo azul

import sys

import pygame


def run_game(title: str = "Tela Azul"):
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    screen_widht = 1200
    screen_height = 800
    bg_color = (0, 0, 80)

    screen = pygame.display.set_mode((screen_widht, screen_height))

    # Janela inteira do jogo
    pygame.display.set_caption(title)

    # Inicia o laço principal do jogo
    while True:
        screen.fill(bg_color)

        for event in pygame.event.get():
            # pygame.event.get() -> acessar todos os eventos detectados
            if event.type == pygame.QUIT:
                # quando o evento for == ao usuário cliclar no botão de fechamento
                sys.exit()

        pygame.display.flip()


run_game()
