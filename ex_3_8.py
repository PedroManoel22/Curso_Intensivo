# 3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
# você gostaria de visitar.
# • Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
# ordem alfabética. ✔️
# • Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
# elegante; basta exibi-la como uma lista Python pura. ✔️
# • Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
# propriamente dita. ✔️
# • Mostre que sua lista manteve sua ordem original exibindo-a. ✔️
# • Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
# ordem da lista original. ✔️
# • Mostre que sua lista manteve sua ordem original exibindo-a novamente. ✔️
# • Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
# que sua ordem mudou. ✔️
# • Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
# mostrar que ela voltou à sua ordem original. ✔️
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética. Exiba a lista para mostrar que sua ordem mudou. ✔️
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou. ✔️
from rich import print

lugares = ['Canadá', 'Tailândia', 'Califórnia', 'Londres', 'Alaska' ]

# Mostrando a lista em ordem original
print(f'\nLista em ordem original: {lugares}')

# Mostrando a lista em ordem alfabética, se alterar a ordem original da lista
print(f'Lista em ordem alfabética, sem alterar a lista original: {sorted(lugares)}')

# Mostrando que a lista não foi alterada
print(f'Mostrando que a ordem da lista não foi alterada: {lugares}')

# Mostrando a lista em ordem alfabética reversa, sem alterar a ordem original da lista
print(f'Ordem alfabética reversa, sem alterar a lista original: {sorted(lugares, reverse=True)}')

# Mostrando que a lista não foi alterada
print(f'Mostrando que a ordem da lista não foi alterada: {lugares}')

# Utilizando o reverse, e mostrando que a ordem da lista foi alterada
lugares.reverse()
print(f'Ultilizando o reverse:')
print(f'Mostrando que a ordem da lista foi alterada: {lugares}')

# Utilizando o reverse novamente, e mostrando que a ordem da lista voltou a ser a original
lugares.reverse()
print(f'Ultilizando o reverse novamente:')
print(f'Mostrando que a ordem da lista voltou a ser a original: {lugares}')

# utilizando sort e mostrando que que sua ordem
lugares.sort()
print(f'Utilizando o sort:')
print(f'Mostrando que a ordem foi alterada: {lugares}')

# utilizando o sort com a opção de inversão
lugares.sort(reverse=True)
print(f'Utilizando o sort com a inversão:')
print(f'Mostrando que a ordem da lista foi alterada: {lugares}')
