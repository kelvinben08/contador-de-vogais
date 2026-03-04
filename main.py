"""
Contador de Vogais

Programa que conta as vogais de um texto.
Versão: 1.1
"""
TAMANHO_LINHA = 78
TITULO = 'Contador de Vogais'
VOGAIS = {'a', 'e', 'i', 'o', 'u'}


def contar_vogais(texto: str) -> int:
    """
    Conta e retorna a quantidade de vogais presentes no texto.

    Args:
        texto (str): texto informado pelo usuário.

    Returns:
        int: quantidade de vogais.
    """
    texto = texto.lower()
    contador = 0

    for letra in texto:
        if letra in VOGAIS:
            contador += 1

    return contador


def contar_vogais_por_tipo(texto: str) -> dict[str, int]:
    """
    Conta e retorna a quantidade de cada vogal presente no texto.

    Args:
        texto (str): texto informado pelo usuário.

    Returns:
        dict: quantidade de cada vogal presente no texto.
    """
    texto = texto.lower()
    vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for letra in texto:
        if letra in vogais:
            vogais[letra] += 1

    return vogais


def main():
    """
    Função principal que executa o fluxo do programa.
    """
    print("=" * TAMANHO_LINHA)
    print(TITULO.center(TAMANHO_LINHA))
    print("=" * TAMANHO_LINHA)

    texto_digitado = input('Digite um texto: ')
    quantidade_vogais = contar_vogais(texto_digitado)

    print(f'O texto digitado contém {quantidade_vogais} vogais.')
    print("=" * TAMANHO_LINHA)
    print('Contagem por vogal:')

    quantidade_cada_vogal = contar_vogais_por_tipo(texto_digitado)

    for chave, valor in quantidade_cada_vogal.items():
        print(f'{chave}: {valor}')

    print("=" * TAMANHO_LINHA)


if __name__ == '__main__':
    main()
