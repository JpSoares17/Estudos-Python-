def main():
    # Leitura:
    numero_1 = int(input("Digite o dividendo: ").strip())
    numero_2 = int(input("Digite o divisor: ").strip())
    # Processamento:
    resto = 0
    while numero_1 >= numero_2:
        numero_1 -= numero_2
        resto = numero_1
    # Saída:
    print(f"Resto da divisão é {resto}")


if __name__ == "__main__":
    main()
