# 2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma
# pessoa em uma variável e então apresente o nome dessa pessoa em letras
# minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.

def valida_nome():
    while True:
        nome = input('Insira seu nome: ')
        
        tem_numero = any(char.isdigit() for char in nome)

        if len(nome) <= 2 or tem_numero:
            print('\n\033[1;31mPor favor insira um nome válido!\033[m\n')
            continue
        
        else:
            return nome


if __name__ == '__main__':
    nome = valida_nome()
    print(f'\nNome: {nome}\n'
          f'Nome com letras minúsculas: {nome.lower()}\n'
          f'Nome com letras maiúsculas: {nome.upper()}\n'
          f'Primeira letra do nome: {nome[0]}\n')