from pathlib import Path

import pygal
from hd_submissions import get_top_submissions
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

submissions_dicts = get_top_submissions()

ROOT_DIR = Path(__file__).parent
FILE_NAME = "resultado_ex17_2.svg"
FILE_DIR = ROOT_DIR / FILE_NAME

# Cria a visualização
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config(
    x_label_rotation=45,
    show_legend=False,
    title_font_size=24,
    label_font_size=14,
    major_label_font_size=18,
    truncate_label=15,
    show_y_guides=False,
    width=1000,
)

chart = pygal.Bar(my_config, style=my_style)

chart.title = "Discussões mais entusiasmadas do momento no Hacker News"
chart.x_labels = [submission_dict["title"] for submission_dict in submissions_dicts]

chart.add(  # type: ignore
    "Comentários",
    [
        {
            "value": submission_dict["label"],
            "xlink": submission_dict["xlink"],
            "label": submission_dict["title"],
        }
        for submission_dict in submissions_dicts
    ],
)
chart.render_to_file(FILE_DIR)  # type: ignore
