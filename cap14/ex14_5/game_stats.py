from settings import Settings


class GameStats:
    """Armazena dados estatísticos da Invasão Alienígena."""

    def __init__(self, ai_settings: Settings) -> None:
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicializa a Invasão Alienígena em um estado ativo
        self.game_active = False

        # Pontuação máxima que não deve ser reiniciada
        self.high_score = self.load_high_score()

    def reset_stats(self) -> None:
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self) -> int:
        """Carrega a pontuação máxima de um arquivo text, ou retorna 0 se não existir."""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0
