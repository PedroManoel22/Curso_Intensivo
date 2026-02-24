# 4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
# (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
# Então faça o seguinte:
# • Adicione uma nova pizza à lista original.
# • Adicione uma pizza diferente à lista friend_pizzas.
# • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
# favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
# mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
# for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja
# armazenada na lista apropriada.

my_pizzas = ['Portuguesa', 'Calabresa', 'Frango', 'Frango com catupiry']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Queijo do reino')
friend_pizzas.append('4 queijos')

# Exibindo a lista das minhas pizzas favoritas
my_pizzas_str = ', '.join(my_pizzas)
print(f'\nMinhas pizzas favoritas são: {my_pizzas_str}')

# Exibindo a lista das pizzas favoritas do meu amigo
friend_pizzas_str = ", ".join(friend_pizzas)
print(f'As pizzas favoritas do meu amigo são: {friend_pizzas_str}')

print('\n')