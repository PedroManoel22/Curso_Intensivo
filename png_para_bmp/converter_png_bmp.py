from pathlib import Path

from PIL import Image


def converter_png_para_bmp(caminho_entrada: str | Path) -> None:
    """
    Converte um arquivo PNG para BMP preservando o nome original.
    """
    # Convertendo para objeto Path para facilitar manipulação de extensões
    path_original = Path(caminho_entrada)

    if path_original.suffix.lower() != ".png":
        print("Erro: O arquivo de entrada deve ser um .png")
        return

    # Define o novo nome trocando a extensão
    path_saida = path_original.with_suffix(".bmp")

    try:
        with Image.open(path_original) as img:
            # O BMP não suporta transparência (Alpha) da mesma forma que o PNG.
            # Convertemos para RGB para evitar cores estranhas ou erros.
            img_rgb = img.convert("RGB")
            img_rgb.save(path_saida, "BMP")
            print(f"Sucesso! Arquivo salvo em: {path_saida}")

    except Exception as e:
        print(f"Erro ao converter: {type(e).__name__} - {e}")


# Exemplo de uso
if __name__ == "__main__":
    converter_png_para_bmp("png_para_bmp/personagem.png")
