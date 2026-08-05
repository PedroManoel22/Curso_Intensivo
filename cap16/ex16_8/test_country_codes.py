import unittest

from country_codes import get_country_code


class CountryCodesTestCase(unittest.TestCase):
    def test_get_country_code(self):
        country_code = get_country_code("Brazil")
        self.assertEqual(country_code, "br")  # Saída esperada: "br"

        country_code = get_country_code("United States")
        self.assertEqual(country_code, "us")  # Saída esperada: "us"

        country_code = get_country_code("Canada")
        self.assertEqual(country_code, "ca")  # Saída esperada: "ca"

        country_code = get_country_code("Nonexistent Country")
        self.assertIsNone(country_code)


if __name__ == "__main__":
    unittest.main()
