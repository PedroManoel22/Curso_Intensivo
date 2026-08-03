import csv
from pathlib import Path

from country_codes import get_country_code

ROOT_DIR = Path(__file__).parent
FILE_NAME = "dados.csv"
ROOT_FILE = ROOT_DIR / FILE_NAME

datas: dict[str, float] = {}


def get_code_expenses() -> dict[str, float]:
    if not ROOT_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ROOT_FILE}")

    with open(ROOT_FILE, encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            if row and row[0] == "Country Name":
                break

        year_index = 65  # 2021
        for row in reader:
            if not row or len(row) <= year_index:
                continue

            country_name = row[0]
            raw_value = row[year_index]

            code = get_country_code(country_name)

            if raw_value.strip() and code:
                try:
                    datas[code] = round(float(raw_value), 2)
                except ValueError:
                    continue

    return datas
