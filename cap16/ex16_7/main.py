import pygal_maps_world.maps
from process_data import ROOT_DIR, get_code_expenses
from pygal.style import LightColorizedStyle as LCS
from pygal.style import RotateStyle as RS

FILE_NAME = "resultado.svg"
ROOT_FILE = ROOT_DIR / FILE_NAME

datas = get_code_expenses()

wm_style = RS("#BA55D3", base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "Government expenditure on education, total (% of GDP) - 2021"
wm.add("Spending on Education (% of GDP)", datas)  # type: ignore

wm.render_to_file(ROOT_FILE)  # type: ignore
