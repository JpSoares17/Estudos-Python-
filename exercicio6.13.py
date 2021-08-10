def main():
    # Processamento:
    temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
    soma = 0
    maximo = temperaturas[0]
    minimo = temperaturas[0]
    for temperatura in temperaturas:
        soma += temperatura
        if temperatura > maximo:
            maximo = temperatura
        elif temperatura < minimo:
            minimo = temperatura
    # Saída:
    print(maximo, minimo, f"{soma / len(temperaturas):.2f}", sep="\n")


if __name__ == "__main__":
    main()
