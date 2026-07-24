from pathlib import Path

import pygal
from random_walk import RandomWalk

diretorio_atual = Path(__file__).parent
print(diretorio_atual)
nome_arquivo = diretorio_atual / "random_walk.svg"

# pyright: reportUnknownMemberType=false

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    visualizacao = pygal.Bar()
    visualizacao.title = "Random Walk"
    visualizacao.x_labels = [str(value) for value in range(rw.num_points)]

    visualizacao.x_title = "Point Number"
    visualizacao.y_title = "Distance from Origin"
    visualizacao.add("Distance", rw.y_values)

    visualizacao.render_to_file(nome_arquivo)

    keep_running = input("Deseja gerar outro passeio aleatório? (s/n): ").strip()
    if keep_running.lower() == "n":
        break
