# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
# uma lista contendo esses itens e então utilize cada função apresentada neste
# capítulo pelo menos uma vez

# As funções são:
# 1. Acessar elementos de uma lista;
# 2. Primeira letra maiúscula
# 3. Modificar um elemento de uma lista;
# 4. Adicionar um elemento ao final da lista;
# 5. Inserir um elemento na lista escolhendo sua posição;
# 6. Remover um elemento da lista escolhendo a posição;
# 7. Remover o último elemento;
# 8. Remover de acordo com o conteúdo;
# 9. Ordem alfabética sem alterar a ordem original da lista;
# 10. Ordem alfabética reversa sem alterar a ordem original da lista;
# 11. Ordem alfabética alterando a ordem original;
# 12. Ordem alfabética reversa alterando a ordem original;
# 13. Reverter a ordem da lista.


cores = ['azul', 'branco', 'vermelho', 'preto', 'cinza', 'marrom', 'amarelo', 'laranja']

# 1.
print(f'1. {cores[2]}')

# 2.
print(f'2. {cores[2].title()}')

# 3.
cores[2] = 'hehehe'
print(f'3. {cores[2]}')

# 4.
cores.append('Adicionando ao final')
print(f'4. {cores}')

# 5.
cores.insert(3, 'Oi')
print(f'5. {cores}')

# 6.
del cores[4]
print(f'6. {cores}')

# 7.
cores.pop()
print(f'7. {cores}')

# 8.
cores.remove('marrom')
print(cores)

# 9.
print(sorted(cores))

# 10.
print(sorted(cores, reverse=True))

# 11.
cores.sort()
print(cores)

# 12.
cores.sort(reverse=True)

# 13.
cores.reverse()
print(cores)
                                  