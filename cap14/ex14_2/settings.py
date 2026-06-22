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
        self.bullet_speed = 8.0
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
