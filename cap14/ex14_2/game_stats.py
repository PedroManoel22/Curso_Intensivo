from __future__ import annotations

from settings import Settings


class GameStats:
    """Acompanha estatísticas do jogo."""

    def __init__(self, settings: "Settings") -> None:
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self) -> None:
        # contador de erros (tiros que saem da tela sem atingir o alvo)
        self.misses_left = self.settings.misses_limit
