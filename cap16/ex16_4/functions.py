from pathlib import Path


def escrever_dados(mes: int, dados: list[dict[str, str]]):
    dados_salvos = Path(__file__).parent
    dados_salvos = dados_salvos / "dados" / f"dados_mes{mes}.csv"

    with open(dados_salvos, "w", encoding="utf-8") as arquivo:
        arquivo.write("Data; Radiação global\n")
        arquivo.writelines(
            f"{item['data']}; {item['Radiação Global']}\n" for item in dados
        )
