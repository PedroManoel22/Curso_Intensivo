# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço parha somente
# dois convidados.
# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas pessoas
# para o jantar.
# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
# apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
# sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
# você sente muito por não poder convidá-la para o jantar.
# • Apresente uma mensagem para cada uma das duas pessoas que continuam na
# lista, permitindo que elas saibam que ainda estão convidadas.
# • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
# tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
# lista vazia no final de seu programa

from rich import print
pessoas = ['Raul Seixas', 'Renato Russo', 'Tim Maia']

for p in pessoas:
    print(f'\n{p}, Vou fazer um jantar delicioso e você está convidado!')

print()
print('[green]Encontrei uma mesa com mais lugares![/]')
pessoas.insert(0, 'Fernandinho')
meio = int(len(pessoas) / 2)
pessoas.insert(meio, 'Claudio')
pessoas.append('José')

for p in pessoas:
    print(f'\n{p}, Vou fazer um jantar delicioso e você está convidado!')

print()
print('[red]Infelizmente não teremos mais nossa mesa, agora nossa mesa terá apenas 2 vagas[/]\n')

# removendo e mandando mensagem de sentimentos para as pessoas removidas

print(pessoas)
pessoas_removidas = ['Fernandinho', 'Claudio', 'José', 'Tim Maia']
for p in pessoas[:]:
    if p in pessoas_removidas:
        pessoas.pop(pessoas.index(p))
        print(f'[purple]{p} me perdoe mas foi não está mais convidado para o jantar![/]\n')

# convite para as duas pessoas restantes

for p in pessoas:
    print(f'Venho aqui lhe convidar Sr(a) {p} para meu jantar ás 19h\n')

del pessoas[0]
del pessoas[0]

print(pessoas)

