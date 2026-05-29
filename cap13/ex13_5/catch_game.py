import game_functions as gf
import pygame
from ball import Ball
from character import Character
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Catch Game - 13.5")

    # Cria o personagem e a bola
    character = Character(screen, ai_settings)
    ball = Ball(screen, ai_settings)

    # Configura o clock para limitar os FPS e o jogo não rodar acelerado demais
    clock = pygame.time.Clock()

    while True:
        gf.check_events(character)
        character.update()
        gf.update_ball(ball, character)
        gf.update_screen(ai_settings, screen, character, ball)

        clock.tick(60)  # Mantém o jogo a 60 frames por segundo


run_game()
