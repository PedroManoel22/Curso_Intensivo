# Escreva um caso de teste para Employee. Crie dois métodos de teste,
# test_give_default_raise() e test_give_custom_raise(). Use o método
# setUp() para que não seja necessário criar uma nova instância de funcionário em
# cada método de teste. Execute seu caso de teste e certifique-se de que os dois
# testes passem.

import unittest

from ex_11_13 import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee1 = Employee("Pedro", "Manoel", 70_000)

    def test_give_default_raise(self):
        result = self.employee1.give_raise()
        expected = (
            "Pedro Manoel, anuual wage = 70000.00 + raise of R$5000.00 = R$75000.00"
        )
        self.assertEqual(result, expected)

    def test_give_custom_raise(self):
        result2 = self.employee1.give_raise(7000)

        expected = (
            "Pedro Manoel, anuual wage = 70000.00 + raise of R$7000.00 = R$77000.00"
        )
        self.assertEqual(result2, expected)


unittest.main()
