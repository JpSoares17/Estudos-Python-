def main():
    # Processamento:
    quantidade = 0
    soma = 0
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1
    media = soma / quantidade
    # Saída:
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")


if __name__ == "__main__":
    main()
