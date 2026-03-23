import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'janis joplin' funcionam ?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")
        # verifica se o resultado recebido é igual ao resultado que esperamos


unittest.main()  # executa os testes
