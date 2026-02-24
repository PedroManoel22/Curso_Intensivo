# 2.3 – Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e
# apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples, como
# “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.

def valida_nome():
    while True:
        nome = input('Insira seu nome: ')
        
        tem_numero = any(char.isdigit() for char in nome)

        if len(nome) <= 2 or tem_numero:
            print('\n\033[1;31mPor favor insira um nome válido!\033[m\n')
            continue
        
        else:
            return nome


apresentar_nome = lambda nome: print(f'\nAlô {nome}, você gostaria de aprender um pouco de Python hoje?\n') 

if __name__ == '__main__':
    nome = valida_nome()
    apresentar_nome(nome)