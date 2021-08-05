def main():
    # Leitura:
    numero = input("Digite um número: ").strip()
    # Processamento:
    base = int(numero)
    comparador = int(numero[::-1])
    # Saída:
    if comparador == base:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")


if __name__ == "__main__":
    main()
