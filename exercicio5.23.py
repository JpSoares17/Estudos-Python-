def main():
    # Leitura:
    numero = int(input("Digite um número: ").strip())
    # Processamento:
    divisor = 2
    while divisor < numero - 1:
        if numero % divisor == 0:
            print("Não é primo!")
            break
        divisor += 1
    if numero % divisor != 0:
        print("É primo!")


if __name__ == "__main__":
    main()
