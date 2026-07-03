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
from scoreboard import Scoreboard
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

    if event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event: pygame.event.Event, ship: Ship):
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

    # Observa eventos de teclado e mouse
    for event in pygame.event.get():
        # pygame.event.get() -> acessar todos os eventos detectados
        if event.type == pygame.QUIT:
            # quando o evento for == ao usuário cliclar no botão de fechamento
            sys.exit()

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

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

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
):
    """Inicia um novo jogo quando o jogador clicar em PLay."""

    botao_clicado = play_button.rect.collidepoint(mouse_x, mouse_y)
    if botao_clicado and not stats.game_active:
        # Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()

        # Oculta o curso do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: "Group[Any]",
    stats: GameStats,
    sb: Scoreboard,
    play_button: Button,
) -> None:
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela a cada passagem pelo laço

    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Desenha a informação sobre pontuação
    sb.show_score()

    # Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()


def update_bullets(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
    stats: GameStats,
    sb: Scoreboard,
):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos"""

    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que despareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)


def check_bullet_alien_collisions(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
    stats: GameStats,
    sb: Scoreboard,
):
    """Respode as colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():  # type: ignore
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        # Destroi os projéteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increse_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: "Group[Any]"
):
    """Dispara um projétil se o limite ainda não foi alcançado."""

    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings: Settings, alien_width: int) -> int:
    available_space_x = ai_settings.screen_widht - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings: Settings, ship_height: int, alien: Alien) -> int:
    """determina o númeoro de linhas com alienígenas que cabem na tela."""
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
):
    # Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(
    ai_settings: Settings, screen: pygame.Surface, ship: Ship, aliens: Group[Any]
):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien)

    # Cria a frota de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings: Settings, aliens: Group[Any]):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_diretion(ai_settings, aliens)
            break


def change_fleet_diretion(ai_settings: Settings, aliens: Group[Any]):
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
):
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
):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # trata esse caso do mesmo jeito que é feito quando a espaçõnave é atingida
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(
    ai_settings: Settings,
    stats: GameStats,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group[Any],
    bullets: Group[Any],
):
    """Verifica se a frota está em uma das bordas
    e então atualiza as posições de todos os alienígenas da frota."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):  # type: ignore
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_butom(ai_settings, stats, screen, ship, aliens, bullets)
