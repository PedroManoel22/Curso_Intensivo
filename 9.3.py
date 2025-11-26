# 9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, então, crie
# vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome
# describe_user() que apresente um resumo das informações do usuário. Escreva outro método chamado greet_user()
# que mostre uma saudação personalizada ao usuário.
# Crie várias instâncias que representem diferentes usuários e chame os dois métodos para cada usuário.

from datetime import datetime

class User:
    def __init__(self):
        self.first_name = 'Pedro'
        self.last_name = 'Miguel'   
        self.age = 18
        self.height = 1.75
        self.nationality = 'Brasileiro'

    def describe_user(self):
        print(f'\n-----user Information-----\n'
                f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'Age: {self.age}\n'
                f'Height: {self.height}\n'
                f'Nationality: {self.nationality}\n')

    def greet_user(self):
        now = datetime.now()
        only_time = now.strftime('%H%M')
        only_time = int(only_time)

        # good morning
        if only_time >= 500 and only_time <= 1159:
            greet = 'good morning'
        
        # good afternoon
        elif only_time >= 1200 and only_time <= 1759:
            greet = 'good afternoon'

        # goodnight
        else:
            greet = 'goodnight'
        
        print(f'{greet} {self.first_name}, welcome!')

user1 = User()
user1.describe_user()
user1.greet_user()
    