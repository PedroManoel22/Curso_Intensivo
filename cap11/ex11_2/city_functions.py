# 11.2 – População: Modifique sua função para que ela exija um terceiro
# parâmetro, population. Agora ela deve devolver uma única string no formato
# Cidade, País – população xxx, por exemplo, Santiago, Chile – população
# 5000000.
# Execute
# test_cities.py
# test_city_country() falhe dessa vez.
# novamente.
# Certifique-se
# de
# que
# Modifique a função para que o parâmetro population seja opcional. Execute
# test_cities.py novamente e garanta que test_city_country() passe novamente.
# Escreva um segundo teste chamado test_city_country_population() que
# verifique se você pode chamar sua função com os valores 'santiago', 'chile' e
# 'population=5000000'. Execute test_cities.py novamente e garanta que esse novo
# teste passe.


def city_country(city: str, country: str, population: str = "") -> str:
    """
    Formata informações de localização geográfica em uma string legível.

    Args:
        city: O nome da cidade.
        country: O nome do país onde a cidade está localizada.
        population: Valor opcional representando a população da cidade.
            Se omitido, o retorno conterá apenas cidade e país.

    Returns:
        Uma string formatada como 'Cidade, País' ou
        'Cidade, País - população X'.

    Example:
        >>> city_country('joão pessoa', 'brasil', '800000')
        'João Pessoa, Brasil - população 800000'
    """

    if population:
        return f"{city.title()}, {country.title()} - população {population}"
    else:
        return f"{city.title()}, {country.title()}"
