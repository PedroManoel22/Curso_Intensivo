# 9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três instâncias diferentes da classe e chame
# describe_restaurant() para cada instância.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(f'\nName: {self.restaurant_name}\n'
              f'type: {self.cuisine_type}')


# Restaurante 1    
restaurant1 = Restaurant('Pedro`s bar', 'Comida nordestina')
restaurant1.describe_restaurant()

# Restaurante 2  
restaurant2 = Restaurant('JOTAKA', 'Sushi')
restaurant2.describe_restaurant()

# Restaurante 3
restaurant3 = Restaurant('Fernandinhos', 'Pizzaria')
restaurant3.describe_restaurant()
