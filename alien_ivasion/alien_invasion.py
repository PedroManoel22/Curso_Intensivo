import sys

import pygame
from settings import Settings


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht, ai_settings.screen_height)
    )  # Janela inteira do jogo
    pygame.display.set_caption("Alien Invasion")

    # Define a cor de fundo

    #            R    G    B
    # bg_color = (230, 230, 230)  # Branco
    # bg_color = (255, 0, 0)  # Vermelho
    # bg_color = (0, 255, 0)  # Verde
    # bg_color = (0, 0, 255)  # Azul

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e mouse
        for event in (
            pygame.event.get()
        ):  # pygame.event.get() -> acessarv todos os eventos detectados
            if (
                event.type == pygame.QUIT
            ):  # quando o evento for == ao usuário cliclar no botão de fechamento
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()
