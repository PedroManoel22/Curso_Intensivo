# 8.7 – Álbum: Escreva uma função chamada make_album() que construa um
# dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
# artista e o título de um álbum e deve devolver um dicionário contendo essas duas
# informações. Use a função para criar três dicionários que representem álbuns
# diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
# armazenando as informações do álbum corretamente.
# Acrescente um parâmetro opcional em make_album() que permita armazenar o
# número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
# para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
# menos uma nova chamada da função incluindo o número de faixas em um álbum.


def make_album(name: str, title: str, tracks: int = 0) -> dict[str, str]:
    album: dict[str, str] = dict()
    album["name"] = name
    album["title"] = title
    if tracks > 0:
        album["tracks"] = str(tracks)
    return album


if __name__ == "__main__":
    album1: dict[str, str] = make_album("João", "1")
    album2 = make_album("Fernando", "Luar")
    album3 = make_album("RT", "Um dois")
    album4 = make_album("RT", "Um dois", 5)

    print(album1)
    print(album2)
    print(album3)
    print(album4)
