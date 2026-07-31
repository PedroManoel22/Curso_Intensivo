from pathlib import Path

import pygal_maps_world.maps
from country_codes import get_country_code
from filtra_dados_pib import filtrar_ultimo_ano

ROOT_DIR = Path(__file__).parent
FILE_NAME = "resultado.svg"
ROOT_FILE = ROOT_DIR / FILE_NAME

dados = filtrar_ultimo_ano()

dados_codigo_pib = {}

for d in dados:
    if "Country Name" in d and "Value" in d:
        country_name = d["Country Name"]
        pib = int(float(d["Value"]))

        code = get_country_code(country_name)

        if code:
            dados_codigo_pib[code] = pib

# --- RENDERIZAÇÃO NO MAPA ---
wm = pygal_maps_world.maps.World()
wm.title = "PIB Mundial em 2014"
wm.add("2014", dados_codigo_pib)  # type: ignore

wm.render_to_file(ROOT_FILE)  # type: ignore
print(f"Sucesso! {len(dados_codigo_pib)} países foram mapeados.")  # type: ignore
