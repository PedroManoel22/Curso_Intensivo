# 4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
# for para fazer exibições a fim de economizar espaço. Escolha uma versão de
# foods.py e escreva dois laços for para exibir cada lista de comidas.

my_pizzas = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_pizzas = ['pizza', 'falafel', 'carrot cake', 'ice cream']

print('\nMinhas pizzas favoritas: ', end='')
for p in my_pizzas:
    print(f'{p} ', end='')

print('\n')

print('Pizzas favoritas do meu amigo: ', end='')
for p in friend_pizzas:
    print(f'{p} ', end='')

print('\n')