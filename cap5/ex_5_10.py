# 5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
# que simule o modo como os sites garantem que todos tenham um nome de usuário
# único.
# • Crie uma lista chamada current_users com cinco ou mais nomes de usuários. ✔️
# • Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que
# um ou dois dos novos usuários também estejam na lista current_users. ✔️
# • Percorra a lista new_users com um laço para ver se cada novo nome de usuário
# já foi usado. Em caso afirmativo, mostre uma mensagem informando que a
# pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado,
# apresente uma mensagem dizendo que o nome do usuário está disponível. ✔️
# • Certifique-se de que sua comparação não levará em conta as diferenças entre
# letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser
# aceito.

from rich import print

current_users = [
    "Pedro123",
    "Jorginho",
    "Paçoca_noturna",
    "Felipinho",
    "Aninha",
    "Mari_edu",
]

current_user = [x.lower() for x in current_users]

new_users = ["Pedro123", "Paçoca_noturna", "AnA"]

new_users = [y.lower() for y in new_users]

print()

for user in new_users:
    while user in current_user:
        new = str(
            input(
                f'O usuário "{user}" já está em uso, por favor insira um novo: '
            )
        ).lower()

        if not new:
            print("\n[red]Por favor insira um nome de usuário![/]\n")

        if new in current_user:
            print(
                f'\nO usuário "{user}" já está em uso, por favor insira um novo: '
            )

        if new in new_users:
            while new in new_users:
                new = str(
                    input(
                        f'\nO usuário "{new}"  está preste a entrar em uso, por favor insira um novo: '
                    )
                )

        if new not in current_user and len(new) > 1:
            new_users.remove(user)
            new_users.insert(0, new)
            break

    if user not in current_user:
        print(f"\n[green]{user} está disponível![/]")
