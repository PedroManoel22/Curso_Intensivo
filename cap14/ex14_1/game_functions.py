from __future__ import annotations

import sys
from time import sleep
from typing import Any

import pygame
from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship


# ---------------------------------------
# Função reutilizável para iniciar o jogo
# ---------------------------------------
def start_game(
    ai_settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    if stats.game_active:
        return
    # Oculta o cursor do mouse
    pygame.mouse.set_visible(False)
    # Reinicia os dados estatísticos
    stats.reset_stats()
    stats.game_active = True
    # Limpa grupos
    aliens.empty()
    bullets.empty()
    # Recria frota e centraliza a nave
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_keydown_events(
    event: pygame.event.Event,
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    bullets: Group[Any],
    stats: GameStats,
    aliens: Group[Any],
) -> None:
    """Responde a pressionamento de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

    # Inicia o jogo ao pressionar "p"
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)


def check_keyup_events(event: pygame.event.Event, ship: Ship) -> None:
    """Responde a solturas de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(
    ai_settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    play_button: Button,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Responde a eventos de pressionamento de teclas e mouse"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Clique do mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                ai_settings,
                screen,
                stats,
                play_button,
                ship,
                aliens,
                bullets,
                mouse_x,
                mouse_y,
            )

        # Tecla pressionada
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event, ai_settings, screen, ship, bullets, stats, aliens
            )

        # Tecla solta
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(
    ai_settings: Settings,
    screen: pygame.Surface,
    stats: GameStats,
    play_button: Button,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
    mouse_x: int,
    mouse_y: int,
) -> None:
    """Inicia um novo jogo quando o jogador clicar em Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)


def update_screen(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
    stats: GameStats,
    play_button: Button,
) -> None:
    """Atualiza as imagens na tela e alterna para a nova tela."""

    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos"""

    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in list(bullets):
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Responde às colisões entre projéteis e alienígenas."""

    pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroi os projéteis existentes e cria uma nova frota
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: Group[Any]
) -> None:
    """Dispara um projétil se o limite ainda não foi alcançado."""

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings: Settings, alien_width: int) -> int:
    available_space_x = ai_settings.screen_widht - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings: Settings, ship_height: int, alien: Alien) -> int:
    """Determina o número de linhas com alienígenas que cabem na tela."""
    alien_height = alien.rect.height
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = available_space_y // (2 * alien_height)
    return number_rows


def create_alien(
    ai_settings: Settings,
    screen: pygame.Surface,
    aliens: Group[Any],
    alien_number: int,
    row_number: int,
) -> None:
    """Cria um alienígena e o posiciona na linha."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, aliens: Group[Any]
) -> None:
    """Cria uma frota completa de alienígenas."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings: Settings, aliens: Group[Any]) -> None:
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_diretion(ai_settings, aliens)
            break


def change_fleet_diretion(ai_settings: Settings, aliens: Group[Any]) -> None:
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(
    ai_settings: Settings,
    stats: GameStats,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena"""

    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Esvazia a lista de alienígenas e de projéteis
    aliens.empty()
    bullets.empty()

    # Cria uma nova frota e centraliza a espaçonave
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_aliens_butom(
    ai_settings: Settings,
    stats: GameStats,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Verifica se algum alienígena alcançou a parte inferior da tela."""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata como quando a espaçonave é atingida
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(
    ai_settings: Settings,
    stats: GameStats,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
) -> None:
    """Verifica bordas e atualiza posições da frota."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica colisão alienígena × nave
    if pygame.sprite.spritecollideany(ship, aliens):  # type: ignore
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Verifica alienígena na parte inferior
    check_aliens_butom(ai_settings, stats, screen, ship, aliens, bullets)
