# 9.14 – Dados: O módulo random contém funções que geram números aleatórios
# de várias maneiras. A função randint() devolve um inteiro no intervalo
# especificado por você. O código a seguir devolve um número entre 1 e 6:
# from random import randint
# x = randint(1, 6)
# Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
# Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e
# o número de lados do dado. Crie um dado de seis dados e lance-o dez vezes.
# Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes.


class Die:
    """
    Esta classe chamada de Die, sorteia números entre 1 e o número de lados de um dado.
    Temos apenas um atributo (sides), cujo seu valor padrão é 6, onde informa quantos
    lados o dado tem.
        Metódos:

            rool_die() -> Sorteia números inteiros entre 1 e o número de lados do dado
    """

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint

        # sorteando números aleatórios em cada jogada
        for _ in range(self.sides):
            x = randint(1, self.sides)
            print(f"{x} ", end=" ")
        print("\n")


def jogar_x_vezes(x: int, dado: Die):
    for i in range(1, x + 1):
        print(f"{i}° jogada:")
        dado.roll_die()


if __name__ == "__main__":
    d1 = Die()
    VEZES = 10

    print(f"\nJogando o dado de 6 lados {VEZES}x!\n")
    jogar_x_vezes(VEZES, d1)

    dado_10_lados = Die(10)
    dado_20_lados = Die(20)

    print(f"\nJogando o dado de 10 lados {VEZES}x!\n")
    jogar_x_vezes(VEZES, dado_10_lados)

    print(f"\nJogando o dado de 20 lados {VEZES}x!\n")
    jogar_x_vezes(VEZES, dado_20_lados)
