from __future__ import annotations  # DEVE SER A LINHA 1

import sys
from typing import Any

import pygame
from bullet import Bullet
from pygame.sprite import Group
from settings import Settings
from ship import Ship

# Tipagem


def check_keydown_events(
    event: pygame.event.Event,
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    bullets: Group[Any],
) -> None:
    """Responde a pressionamento de tecla."""

    if event.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move a espaçonave para a esquerda
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event: pygame.event.Event, ship: Ship):
    """Responde a solturas de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: Group[Any]
) -> None:
    """Responde a eventos de pressionamento de teclas e mouse"""

    # Observa eventos de teclado e mouse
    for event in pygame.event.get():
        # pygame.event.get() -> acessar todos os eventos detectados
        if event.type == pygame.QUIT:
            # quando o evento for == ao usuário cliclar no botão de fechamento
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: "Group[Any]"
) -> None:
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
