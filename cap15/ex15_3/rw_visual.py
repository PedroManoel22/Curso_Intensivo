import matplotlib.pyplot as plt
from random_walk import RandomWalk

# pyright: reportUnknownMemberType=false

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(dpi=128, figsize=(10, 6))

    # Plota os pontos e mostra o gráfico
    point_numbers = list(range(rw.num_points))
    plt.plot(
        rw.x_values,
        rw.y_values,
        linewidth=5,
    )

    plt.show()

    keep_running = input("Deseja gerar outro passeio aleatório? (s/n): ").strip()
    if keep_running.lower() == "n":
        break
