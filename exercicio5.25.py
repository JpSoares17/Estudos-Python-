def main():
    # Leitura:
    numero = int(input("Digite um número: ").strip())
    # Processamento:
    base = 2
    while True:
        p = (base + (numero / base)) / 2
        base = p
        if p ** 2 - numero < 0.0001 and p ** 2 > numero:
            break
        if numero - p ** 2 < 0.0001 and numero > p ** 2:
            break
    # Saída:
    print(f"Raiz quadrada de {numero} é {p}")


if __name__ == "__main__":
    main()
