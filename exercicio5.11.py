def main():
    # Leitura:
    valor_inicial = float(input("Digite depósito inicial: ").strip())
    taxa_juros = float(input("Digite a taxa de juros: ").strip())
    # Processamento:
    meses = 1
    montante = valor_inicial
    while meses <= 24:
        montante += (montante * (taxa_juros / 100))
        meses += 1
    # Saída:
    print(f"Seu montante: {montante:.2f}")


if __name__ == "__main__":
    main()
