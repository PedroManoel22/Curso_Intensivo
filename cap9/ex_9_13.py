# 9.13 – Reescrevendo o programa com OrderedDict: Comece com o Exercício
# 6.4 (página 155), em que usamos um dicionário-padrão para representar um
# glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
# que a ordem da saída coincida com a ordem em que os pares chave-valor foram
# adicionados ao dicionário.


class OderedDict:
    def __init__(self, **glossary):
        self.glossary = glossary

    def show_glossario(self):
        print()
        for k, v in self.glossary.items():
            print(f"{k} -> {v}")
        print()


if __name__ == "__main__":
    glosario = {
        "Print": "Imprime algo no terminal",
        "Input": "Recebe algo do usuário",
        "Variável": "Um endereço na memória que recebe um valor",
        "String": "Uma variável, do tipo texto",
        "Int": "Uma variável, número (ex: 5) do tipo inteiro ",
        "Float": "Uma variável, número (com ponto flutuante. ex: 1.5) do tipo float",
        "Loop": "Estrutura de repetição, ex: for, while",
        "Classe": "Modelo para criar objetos",
        "Função": "Bloco de código reutilizável",
        "Comentário": "Texto ignorado pelo interpretador, iniciado com #  ou '''",
    }

    g1 = OderedDict(**glosario)
    g1.show_glossario()
