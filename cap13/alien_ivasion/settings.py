class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self) -> None:
        """Inicializa as configurações do jogo."""

        # Configurações da tela

        self.screen_widht = 640
        self.screen_height = 360

        # Define a cor de fundo
        self.bg_color = (0, 0, 80)
        #            R    G    B
        # bg_color = (230, 230, 230)  # Branco
        # bg_color = (255, 0, 0)  # Vermelho
        # bg_color = (0, 255, 0)  # Verde
        # bg_color = (0, 0, 255)  # Azul

        # Configurações da espaçonave
        self.ship_speed_factor = 1

        # configurações dos projéteis
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 165, 0
        self.bullets_allowed = 3

        # Configuração dos alienígenas
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 8
        # fleet_direction igual a 1 representa a direita; -1 representa
        # a esquerda
        self.fleet_direction = 1
