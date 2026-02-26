# 6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
# • Crie uma lista de pessoas que devam participar da enquete sobre linguagem
# favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
# estão. ✔️
# • Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
# respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
# Se ainda não participaram da enquete, apresente uma mensagem convidando-as
# a responder. ✔️

from rich import print

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people_participate = ["jen", "pedro", "sarah", "jose", "phil"]

print()

for p in people_participate:
    if p in favorite_languages.keys():
        print(f"[green1]Obrigado {p} por participar da enquete![/]\n")

    else:
        print(
            f"[yellow]{p}, você tem interesse em participar da nossa enquete?[/]\n"
        )

print()
