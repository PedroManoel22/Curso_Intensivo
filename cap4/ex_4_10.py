# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
# acrescente várias linhas no final do programa que façam o seguinte:
# • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
# para exibir os três primeiros itens da lista desse programa.
# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três
# itens do meio da lista.
# • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir
# os três últimos itens da lista.

multiplos_tres = [x for x in range(3, 31, 3)]

print('\nOs três primeiros itens da lista são: ', end='')

# Exibindo os três primeiros elementos (números) da lista
for n in multiplos_tres[:3]:
    print(f'{n} ', end='')

print('\n')

print('Os três últimos itens da lista são: ', end='')

# Exibindo os três últimos elementos (números) da lista
for n in multiplos_tres[-3:]:
    print(f'{n} ', end='')

print('\n')