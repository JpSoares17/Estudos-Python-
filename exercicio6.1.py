def main():
    # Processamento:
    notas = [0, 0, 0, 0, 0, 0, 0]
    soma = 0
    indice = 0
    while indice < 7:
        # Leitura:
        notas[indice] = float(input("Digite uma nota: ").strip())
        soma += notas[indice]
        indice += 1
    indice = 0
    while indice < 7:
        # Saída:
        print(f"Nota {indice}: {notas[indice]:6.2f}")
        indice += 1
    print(f"Média: {soma / indice:5.2f}")


if __name__ == "__main__":
    main()
