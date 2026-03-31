# 12.2 – Personagem do jogo: Encontre uma imagem de bitmap de um personagem
# de jogo que você goste ou converta uma imagem em um bitmap. Crie uma classe
# que desenhe o personagem no centro da tela e faça a cor de fundo da imagem
# coincidir com a cor de fundo da tela ou vice-versa.

import sys

import pygame


class Ship:
    def __init__(self, screen: pygame.Surface) -> None:
        """Inicializa a imagem e define sua posição inicial."""
        self.screen = screen

        # Carega a imagem da personagem e obtém seu rect
        self.image = pygame.image.load(
            "Curso_Intensivo/png_para_bmp/personagem.bmp"
        ).convert_alpha()
        # Carregando a imagem

        self.rect = self.image.get_rect()  # Pegando o rect da imagem
        self.screen_rect = screen.get_rect()  # Pegando o rect da tela

        # Inicia cada nova personagem no meio da tela
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Desenha a personagem em sua posição atual."""
        self.screen.blit(self.image, self.rect)


def run_game(title: str = "Tela com a personagem"):
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    screen_widht = 1200
    screen_height = 800
    bg_color = (86, 125, 96)

    screen = pygame.display.set_mode((screen_widht, screen_height))

    ship = Ship(screen)  # criando a personagem

    # Janela inteira do jogo
    pygame.display.set_caption(title)

    # Inicia o laço principal do jogo
    while True:
        screen.fill(bg_color)
        ship.blitme()

        for event in pygame.event.get():
            # pygame.event.get() -> acessar todos os eventos detectados
            if event.type == pygame.QUIT:
                # quando o evento for == ao usuário cliclar no botão de fechamento
                sys.exit()

        pygame.display.flip()


run_game()
