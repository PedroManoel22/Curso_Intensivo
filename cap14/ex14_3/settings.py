from __future__ import annotations


class Settings:
    """Armazena as configurações do jogo."""

    def __init__(self) -> None:
        # Tela
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (30, 30, 40)

        # Nave
        self.ship_speed = 4.0

        # Projéteis
        self.bullet_speed = 20
        self.bullet_width = 6
        self.bullet_height = 2
        self.bullet_color = (255, 230, 120)
        self.bullets_allowed = 4

        # Alvo
        self.target_speed = 3.0
        self.target_width = 18
        self.target_height = 120
        self.target_color = (120, 200, 255)

        # Limite de erros (tiros perdidos que passam da tela)
        self.misses_limit = 3

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self) -> None:
        """Inicializa as configurações que mudam no decorrer do jogo."""

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda.
        self.fleet_direction = 1

    def increse_speed(self) -> None:
        """Aumenta as configurações de velocidade e o valor dos pontos."""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
