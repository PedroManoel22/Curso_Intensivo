from random import randint


class Die:
    """Uma classe para simular um único dado."""

    def __init__(self, num_sides: int = 6):
        """Supõe uqe seja um dado de seis lados."""
        self.num_sides = num_sides

    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self.num_sides)
