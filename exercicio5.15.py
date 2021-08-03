def main():
    # Processamento:
    valor = 0
    while True:
        codigo = int(input("Digite o código do produto: ").strip())
        if codigo == 1:
            valor += 0.5
        if codigo == 2:
            valor += 1
        if codigo == 3:
            valor += 4
        if codigo == 5:
            valor += 7
        if codigo == 9:
            valor += 8
        if codigo == 0:
            break
        if codigo not in (1, 2, 3, 5, 9, 0):
            print("Digite um codigo válido")
    # Saída:
    print(f"Total: R${valor:.2f}")


if __name__ == "__main__":
    main()
