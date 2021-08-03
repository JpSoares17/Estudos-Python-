def main():
    # Leitura:
    divida_mensal = float(input("Valor inicial da dívida: ").strip())
    taxa_mensal = float(input("Taxa de juros: ").strip())
    pagamento_mensal = float(input("Valor pago mensalmente: ").strip())
    # Processamento:
    meses = 0
    total_pago = 0
    juros_total = 0
    while divida_mensal > 0:
        divida_mensal -= pagamento_mensal
        total_pago += pagamento_mensal
        juros_total += divida_mensal * (taxa_mensal / 100)
        divida_mensal += divida_mensal * (taxa_mensal / 100)
        meses += 1
    # Saída:
    print(f"Meses para ser pago: {meses}")
    print(f"Total pago: R${total_pago:.2f}")
    print(f"Juros pago: R${juros_total:.2f}")


if __name__ == "__main__":
    main()
