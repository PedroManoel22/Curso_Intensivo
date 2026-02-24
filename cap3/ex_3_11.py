# 3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
# seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em um
# de seus programas de modo a gerar um erro de índice. Não se esqueça de corrigir
# o erro antes de fechar o programa.

# peguei o programa do exercício 3.4

pessoas = ['Raul Seixas', 'Renato Russo', 'Tim Maia']

for p in pessoas:
    print(f'\n{p}, Vou fazer um almoço delicioso e você está convidado!')

print()
print(pessoas[3]) # grenaod o erro de índice, a lista "pessoas" tem índice 2

