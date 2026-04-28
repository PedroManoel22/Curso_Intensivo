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

    if event.key == pygame.K_DOWN:
        # Move a espaçonave para baixo
        ship.moving_down = True

    elif event.key == pygame.K_UP:
        # Move a espaçonave para cima
        ship.moving_up = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event: pygame.event.Event, ship: Ship):
    """Responde a solturas de tecla."""

    if event.key == pygame.K_DOWN:
        ship.moving_down = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False


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


def update_bullets(ai_settings: Settings, bullets: Group[Any]):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos"""

    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que despareceram
    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_widht:
            bullets.remove(bullet)


def fire_bullet(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: "Group[Any]"
):
    """Dispara um projétil se o limite ainda não foi alcançado."""

    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
