# 5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
# lista de usuários não esteja vazia.
# • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
# usuários!
# • Remova todos os nomes de usuário de sua lista e certifique-se de que a
# mensagem correta seja exibida.

user_names = ["Pedro", "João", "Admin", "Lucas", "Fernando"]
# user_names = []

if user_names:
    print("A lista não está vazia!")

elif not user_names:
    print("Prescisamos encontrar alguns usuários!")
