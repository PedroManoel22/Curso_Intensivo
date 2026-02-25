# 5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o
# nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma
# saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista
# com um laço e mostre uma saudação para cada usuário:
# • Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo,
# Olá admin, gostaria de ver um relatório de status?
# • Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
# fazer login novamente.

user_names = ["Pedro", "João", "Admin", "Lucas", "Fernando"]

for user in user_names:
    if user == "Admin":
        print(f"\nOlá {user}, gostaria de ver um relatório de status?")

    else:
        print(f"\nOlá {user}, obrigado por fazer login novamente!")
print()
