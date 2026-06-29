from __future__ import annotations

import sys
from typing import Any

import pygame
from bullet import Bullet
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from target import Target


# ------------------------
# Fluxos principais
# ------------------------
def start_game(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
) -> None:
    """Prepara um novo jogo."""
    if stats.game_active:
        return

    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    bullets.empty()
    ship.center_ship()
    # Recentraliza o alvo também
    target.rect.midright = (screen.get_rect().right - 10, screen.get_rect().centery)
    target.y = float(target.rect.y)
    target.direction = 1


def end_game(stats: GameStats) -> None:
    """Finaliza o jogo e mostra cursor/botão."""
    stats.game_active = False
    pygame.mouse.set_visible(True)


# ------------------------
# Entrada do usuário
# ------------------------
def check_keydown_events(
    event: pygame.event.Event,
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
) -> None:
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE and stats.game_active:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        start_game(settings, screen, stats, ship, bullets, target)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event: pygame.event.Event, ship: Ship) -> None:
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    play_button: Button,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, ship, bullets, target)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                settings,
                screen,
                stats,
                play_button,
                ship,
                bullets,
                target,
                mouse_x,
                mouse_y,
            )


def check_play_button(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    play_button: Button,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
    mouse_x: int,
    mouse_y: int,
) -> None:
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # Reinicia as configurações do jogo
        settings.initialize_dynamic_settings()
        start_game(settings, screen, stats, ship, bullets, target)


# ------------------------
# Atualizações
# ------------------------
def fire_bullet(
    settings: Settings, screen: pygame.Surface, ship: Ship, bullets: Group[Any]
):
    """Cria um projétil se abaixo do limite."""
    if len(bullets) < settings.bullets_allowed:
        bullets.add(Bullet(settings, screen, ship))


def update_bullets(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    bullets: Group[Any],
    target: Target,
) -> None:
    """Atualiza projéteis, remove fora da tela e checa colisões."""
    bullets.update()

    # Remover projéteis que saíram da tela (conta como erro)
    for bullet in list(bullets):
        if bullet.rect.left >= screen.get_rect().right:
            bullets.remove(bullet)
            if stats.game_active:
                stats.misses_left -= 1
                if stats.misses_left <= 0:
                    end_game(stats)

    # Colisão projétil × alvo (remove projétil e 'reseta' o alvo de leve)
    for bullet in pygame.sprite.spritecollide(target_as_sprite(target), bullets, True):  # type:ignore
        settings.increse_speed()

        # Para simplificar, apenas inverte a direção ao ser atingido
        target.direction *= -1


def target_as_sprite(target: Target) -> pygame.sprite.Sprite:
    """Adapter leve para usar rect do Target com as funções de colisão."""
    s = pygame.sprite.Sprite()
    s.rect = target.rect  # type: ignore[attr-defined]
    return s


def update_screen(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    play_button: Button,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
) -> None:
    screen.fill(settings.bg_color)

    # Desenhos
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    target.draw()

    # HUD simples: erros restantes
    _draw_misses_hud(screen, stats)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def _draw_misses_hud(screen: pygame.Surface, stats: GameStats) -> None:
    font = pygame.font.SysFont(None, 28)
    text = font.render(f"Erros restantes: {stats.misses_left}", True, (220, 220, 220))
    rect = text.get_rect()
    rect.topleft = (12, 10)
    screen.blit(text, rect)


def update_all(
    settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    ship: Ship,
    bullets: Group[Any],
    target: Target,
) -> None:
    """Atualiza entidades quando o jogo está ativo."""
    if stats.game_active:
        ship.update()
        target.update()
        update_bullets(settings, screen, stats, bullets, target)
