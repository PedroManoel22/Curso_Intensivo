# 3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
# Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
# informando o número de pessoas que você está convidando para o jantar.

from rich import print
#  ex 3.4


# pessoas = ['Raul Seixas', 'Renato Russo', 'Tim Maia']

# for p in pessoas:
#     print(f'\n{p}, Vou fazer um almoço delicioso e você está convidado!')

# print(f'\nEstou chamando {len(pessoas)} para o jantar!')
# print()

# ex 3.5


# pessoas = ['Raul Seixas', 'Renato Russo', 'Tim Maia']

# cabecalho = f'Vou fazer um jantar delicioso e você está convidado!, confira seu nome na lista:\n'

# print(cabecalho)
# for p in pessoas:
#     print(p)
    

# print()
# print(f'[red]{pessoas[1]} não poderá comparecer!\n\033[/]')
# pessoas[1] = 'Joelma'

# print(cabecalho)

# for p in pessoas:
#     print(p)

# print(f'Estou chamando {len(pessoas)} para o jantar!')
# print()


# ex 3.6


# pessoas = ['Raul Seixas', 'Renato Russo', 'Tim Maia']

# for p in pessoas:
#     print(f'\n{p}, Vou fazer um jantar delicioso e você está convidado!')

# print()
# print('\033[1;32mEncontrei uma mesa com mais lugares!\033[m')
# pessoas.insert(0, 'Fernandinho')
# meio = int(len(pessoas) / 2)
# pessoas.insert(meio, 'Claudio')
# pessoas.append('José')

# for p in pessoas:
#     print(f'\n{p}, Vou fazer um jantar delicioso e você está convidado!')

# print(f'Estou chamando {len(pessoas)} para o jantar!')
# print()

# # ex 3.7


# print()
# print('[green]Encontrei uma mesa com mais lugares![/]')
# pessoas.insert(0, 'Fernandinho')
# meio = int(len(pessoas) / 2)
# pessoas.insert(meio, 'Claudio')
# pessoas.append('José')

# for p in pessoas:
#     print(f'\n{p}, Vou fazer um jantar delicioso e você está convidado!')

# print()
# print('[red]Infelizmente não teremos mais nossa mesa, agora nossa mesa terá apenas 2 vagas[/]\n')

# # removendo e mandando mensagem de sentimentos para as pessoas removidas

# print(pessoas)
# pessoas_removidas = ['Fernandinho', 'Claudio', 'José', 'Tim Maia']
# for p in pessoas[:]:
#     if p in pessoas_removidas:
#         pessoas.pop(pessoas.index(p))
#         print(f'[purple]{p} me perdoe mas foi não está mais convidado para o jantar![/]\n')

# # convite para as duas pessoas restantes

# for p in pessoas:
#     print(f'Venho aqui lhe convidar Sr(a) {p} para meu jantar ás 19h\n')

# del pessoas[0]
# del pessoas[0]

# print(pessoas)
# print(f'Estou chamando {len(pessoas)} para o jantar!')

