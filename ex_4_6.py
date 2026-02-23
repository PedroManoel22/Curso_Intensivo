# 4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
# uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os
# números.

num_impares = [x for x in range(1, 21, 2)]
print('\nNúmeros Ímpares de 1 a 20:')
for num in num_impares:
    print(num)