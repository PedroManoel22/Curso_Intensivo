import sys

import pygame
from ball import Ball
from character import Character
from settings import Settings


def check_keydown_events(event: pygame.event.Event, character: Character):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        character.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        character.moving_left = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event: pygame.event.Event, character: Character):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        character.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        character.moving_left = False


def check_events(character: Character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)


def update_ball(ball: Ball, character: Character):
    ball.update()

    # 1. Testa se o jogador "agarrou" a bola (Colisão de retângulos)
    if character.rect.colliderect(ball.rect):
        ball.reset_ball()

    # 2. Testa se a bola desapareceu na parte inferior da tela
    elif ball.rect.top >= ball.screen_rect.bottom:
        ball.reset_ball()


def update_screen(
    ai_settings: Settings, screen: pygame.Surface, character: Character, ball: Ball
):
    screen.fill(ai_settings.bg_color)
    character.draw()
    ball.draw()
    pygame.display.flip()
