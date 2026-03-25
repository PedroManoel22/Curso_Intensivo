# Crie um arquivo de nome test_cities.py que teste a função que você acabou de
# escrever (lembre-se de que é necessário importar unittest e a função que você
# quer testar). Escreva um método chamado test_city_country() para conferir se a
# chamada à sua função com valores como 'santiago' e 'chile' resulta na string
# correta. Execute test_cities.py e garanta que test_city_country() passe no teste.

import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_cities = city_country("santiago", "chile")
        self.assertEqual(formatted_cities, "Santiago, Chile")


unittest.main()
