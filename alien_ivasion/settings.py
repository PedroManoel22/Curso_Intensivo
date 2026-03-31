class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self) -> None:
        """Inicializa as configurações do jogo."""

        # Configurações da tela

        self.screen_widht = 1200
        self.screen_height = 800

        # Define a cor de fundo
        self.bg_color = (0, 0, 80)
        #            R    G    B
        # bg_color = (230, 230, 230)  # Branco
        # bg_color = (255, 0, 0)  # Vermelho
        # bg_color = (0, 255, 0)  # Verde
        # bg_color = (0, 0, 255)  # Azul
