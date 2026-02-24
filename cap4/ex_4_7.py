# 4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
# exibir os números de sua lista.

multiplos_tres = [x for x in range(3, 31, 3)]
print('\nMúltiplos de Três de 3 a 30:')
for multiplo in multiplos_tres:
    print(multiplo)
