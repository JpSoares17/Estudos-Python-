def main():
    # Leitura:
    frase = input("Digite uma frase: ").strip().lower()
    # Processamento:
    contador = {}
    for letra in frase:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    # Saída:
    for chave in contador:
        print(f"{chave}: {contador[chave]}")


if __name__ == "__main__":
    main()
