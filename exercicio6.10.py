def main():
    # Leitura:
    palavra_chave1 = int(input("Digite o valor a procura: ").strip())
    palavra_chave2 = int(input("Digite outro valor a procurar: ").strip())
    # Processamento:
    banco_de_dados = [15, 20, 84, 73]
    x = 0
    posicao = 0
    while x < len(banco_de_dados):
        if banco_de_dados[x] == palavra_chave1:
            posicao += 1
            print(f"{palavra_chave1}, foi o {posicao}º a ser", end=" ")
            print(f"encontrado, na posição {x+1}")
        elif banco_de_dados[x] == palavra_chave2:
            posicao += 1
            print(f"{palavra_chave2}, foi o {posicao}º a ser", end=" ")
            print(f"encontrado, na posição {x+1}")
        x += 1
    if palavra_chave1 not in banco_de_dados:
        print(f"{palavra_chave1} não foi encontrado no banco de dados!")
    if palavra_chave2 not in banco_de_dados:
        print(f"{palavra_chave2} não foi encontrado no banco de dados!")


if __name__ == "__main__":
    main()
