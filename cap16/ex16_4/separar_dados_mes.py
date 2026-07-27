import csv
from pathlib import Path

from Curso_Intensivo.cap16.ex16_4.functions import escrever_dados

ROOT_DIR = Path(__file__).parent
filename = "INMET_CO_DF_A001_BRASILIA_01-01-2026_A_30-06-2026.CSV"
file_dir = ROOT_DIR / filename

with open(file_dir, encoding="latin-1") as f:
    reader = csv.reader(f, delimiter=";")
    # header_now = next(reader)

    # Pula as 8 linhas de metadados do topo
    for _ in range(8):
        next(reader)

    # Guarda o cabeçalho real da tabela (Linha 9: Data, Hora UTC, PRECIPITAÇÃO, etc.)
    header_now = next(reader)

    # print(header_now)

    dados: list[dict[str, str]] = []
    mes_atual = 1

    for row in reader:
        if row:
            data = row[0]
            mes = int(data[5:7])

            if mes != mes_atual:
                # Salva os dados acumulados do mês que acabou
                escrever_dados(mes_atual, dados)
                # Limpa a lista para o novo mês e atualiza o marcador
                dados = []
                mes_atual = mes

            dados.append({"data": data, "Radiação Global": row[6]})

    # Salva os dados do último mês (mês 6) acumulados na lista
    if dados:
        escrever_dados(mes_atual, dados)
