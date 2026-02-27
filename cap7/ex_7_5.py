# 7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
# anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
# custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
# Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
# o preço do ingresso do cinema.

from ex_7_2 import valida_num_int
from rich import print

while True:
    idade = valida_num_int(pergunta="\nInsira sua idade: ")
    if idade == 0:
        break

    elif idade < 3 and idade > 0:
        print(
            f"\nComo a pessoa tem {idade} anos, o ingresso é [green]gratuito[/]!"
        )

    elif idade >= 3 and idade <= 12:
        print(
            f"\nComo a pessoa tem {idade} anos, o ingresso é [green]US$10[/]!"
        )

    else:
        print(
            f"\n como a pessoa tem {idade} anos, o ingresso é [green]US$15[/]!"
        )
