import json
from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILE_NAME = "PIB.json"
ROOT_FILE = ROOT_DIR / FILE_NAME


def filtrar_ultimo_ano():
    with open(ROOT_FILE) as file:
        reader = json.load(file)

    valores: list[dict[str, str]] = []

    for d in reader:
        for v in d.values():
            if v == "2014":
                valores.append(d)

    return valores
