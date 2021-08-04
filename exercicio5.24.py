def eh_primo(n):
    primo = True
    for divisores in range(n - 1, 1, - 1):
        if n % divisores == 0:
            primo = False
    return primo


def main():
    # Leitura:
    numeros = int(input("Digite um número: ").strip())
    # Processamento:
    print("Números primos:")
    for numero in range(1, numeros):
        if eh_primo(numero + 1):
            print("|", numero + 1, end=" | ")


if __name__ == "__main__":
    main()
