import sys

import pygame

# Tipagem
from settings import Settings
from ship import Ship


def check_events() -> None:
    """Responde a ecentos de pressionamento de teclas e mouse"""
    # Observa eventos de teclado e mouse
    for event in pygame.event.get():
        # pygame.event.get() -> acessar todos os eventos detectados
        if event.type == pygame.QUIT:
            # quando o evento for == ao usuário cliclar no botão de fechamento
            sys.exit()


def update_screen(ai_settings: Settings, screen: pygame.Surface, ship: Ship) -> None:
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
