def contar_vogais(texto: str) -> int:
    """
    Conta e retorna a quantidade de vogais presentes no texto.

    Args:
        texto (str): texto informado pelo usuário.

    Returns:
        int: quantidade de vogais.
    """
    texto = texto.lower()
    VOGAIS = {'a', 'e', 'i', 'o', 'u'}
    contador = 0

    for letra in texto:
        if letra in VOGAIS:
            contador += 1

    return contador


def main():
    """
    Função principal que executa o fluxo do programa.
    """
    texto_digitado = input('Digite um texto: ')
    quantidade_vogais = contar_vogais(texto_digitado)
    print(f'O texto digitado contém {quantidade_vogais} vogais.')


if __name__ == '__main__':
    main()
