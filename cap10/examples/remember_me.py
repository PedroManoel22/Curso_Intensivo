import json

# Carrega o nome do usuário se foi armazenado anteriormente
# Caso contrário, pede que o usuário forneça o nome e armazena essa informação


def get_strored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_strored_username()

    if username:
        print("Wecolme back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
