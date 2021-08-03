def main():
    # Leitura:
    valor_inicial = float(input("Digite depósito inicial: ").strip())
    taxa_juros = float(input("Digite a taxa de juros: ").strip())
    deposito_mensal = float(input(
        "Digite o valor que será adicionado mensalmente: ").strip())
    # Processamento:
    meses = 1
    montante = valor_inicial
    while meses <= 24:
        montante += (montante * (taxa_juros / 100)) + deposito_mensal
        meses += 1
    # Saída:
    print(f"Seu montante: R${montante:.2f}")


if __name__ == "__main__":
    main()
