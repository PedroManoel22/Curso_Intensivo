from operator import itemgetter
from typing import Any

import requests

# Faz uma chamada de API e armazena a resposta
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}", "-> Top stories retrieved successfully\n")


def get_top_submissions() -> list[dict[str, Any]]:
    # Processa informações sobre cada artigo submetido
    submission_ids = r.json()
    submissions_dicts: list[dict[str, Any]] = []

    for submission_id in submission_ids[:30]:
        # Cria uma chamada de API separada para cada artigo submetido
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        submission_r = requests.get(url)
        response_dict = submission_r.json()

        print(
            "Status code:",
            submission_r.status_code,
            "-> Title: ",
            response_dict["title"],
            "\n",
        )

        submission_dict: dict[str, Any] = {
            "title": response_dict["title"],
            "xlink": "http://news.ycombinator.com/item?id=" + str(submission_id),
            "label": int(response_dict.get("descendants", 0)),
        }
        submissions_dicts.append(submission_dict)

        submissions_dicts = sorted(
            submissions_dicts, key=itemgetter("label"), reverse=True
        )

    for submission_dict in submissions_dicts:
        print("\nTitle:", submission_dict["title"])
        print("Discussion link:", submission_dict["xlink"])
        print("Comments:", submission_dict["label"])

    return submissions_dicts


if __name__ == "__main__":
    submissions_dicts = get_top_submissions()
