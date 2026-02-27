# 7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5
# que faça o seguinte, pelo menos uma vez:
# • use um teste condicional na instrução while para encerrar o laço;
# • use uma variável active para controlar o tempo que o laço executará;
# • use uma instrução break para sair do laço quando o usuário fornecer o valor
# 'quit'


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
