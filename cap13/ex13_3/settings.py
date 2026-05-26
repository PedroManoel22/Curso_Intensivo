class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self) -> None:
        """Inicializa as configurações do jogo."""

        # Configurações da tela

        self.screen_width: int = 1200
        self.screen_height: int = 800

        # Define a cor de fundo
        self.bg_color = (0, 0, 95)
        #            R    G    B
        # bg_color = (230, 230, 230)  # Branco
        # bg_color = (255, 0, 0)  # Vermelho
        # bg_color = (0, 255, 0)  # Verde
        # bg_color = (0, 0, 255)  # Azul

        # Configuração das gotas
        self.drop_speed_factor = 6
        self.fleet_drop_speed = 10

        # fleet_direction igual a 1 representa a direita; -1 representa
        # a esquerda

        self.fleet_direction = 1
