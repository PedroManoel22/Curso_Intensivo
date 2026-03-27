import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    # Lembrando que os teste devem começar com test_, para que seja executado automaticamente
    def test_first_last_name(self):
        """Nomes como 'janis joplin' funcionam ?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")
        # verifica se o resultado recebido é igual ao resultado que esperamos

    def test_first_last_middle_name(self):
        """Nome como 'Wolfgang Amadeus mozart' funcionam?"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()  # executa os testes
