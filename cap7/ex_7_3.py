# 7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
# número é múltiplo de dez ou não.
from rich import print
from ex_7_2 import valida_num_int

multiplo = 10
num = valida_num_int(pergunta="\nInsira um número inteiro: ")


if num % multiplo == 0:
    print(f"\n[green]{num} é multiplo de {multiplo}![/]\n")

else:
    print(f"\n[red]{num} Não é multiplo de {multiplo}![/]\n")
