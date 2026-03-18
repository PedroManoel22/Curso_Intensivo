# 7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
# férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
# visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
# apresente os resultados da enquete.

dados: list[dict[str, str]] = []

while True:
    pessoa = {
        "nome": input("\nInsira seu nome: ").strip(),
        "lugar_favorito": input(
            "Se pudesse visitar um lugar do mundo, para onde iria? "
        ).strip(),
    }

    dados.append(pessoa)

    continuar = input("Deseja cadastrar mais alguém? [S/N]: ").upper()
    if continuar == "N":
        break

print("\nResultado da enquete:")
for d in dados:
    for k, v in d.items():
        print(k, v)
