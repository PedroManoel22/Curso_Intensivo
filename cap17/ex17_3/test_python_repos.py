import unittest

import requests


class TestPythonRepos(unittest.TestCase):
    """Testes para a chamada de API do GitHub em python_repos.py."""

    @classmethod
    def setUpClass(cls):
        """Faz a chamada de API uma única vez para todos os testes."""
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        cls.r = requests.get(url)
        cls.response_dict = cls.r.json()

    def test_status_code(self):
        """Verifica se a chamada de API foi bem-sucedida (200)."""
        self.assertEqual(self.r.status_code, 200)

    def test_items_returned(self):
        """Verifica se o número de itens devolvidos é o esperado (30, padrão da API)."""
        self.assertEqual(len(self.response_dict["items"]), 30)

    def test_total_repositories(self):
        """Verifica se o total de repositórios é maior que um valor mínimo esperado."""
        self.assertGreater(self.response_dict["total_count"], 1000000)

    def test_response_has_expected_keys(self):
        """Verifica se a resposta contém as chaves esperadas."""
        self.assertIn("items", self.response_dict)
        self.assertIn("total_count", self.response_dict)

    def test_first_repo_has_stargazers_count(self):
        """Verifica se cada repositório retornado tem a contagem de estrelas."""
        first_repo = self.response_dict["items"][0]
        self.assertIn("stargazers_count", first_repo)
        self.assertIsInstance(first_repo["stargazers_count"], int)


if __name__ == "__main__":
    unittest.main()
