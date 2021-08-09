def main():
    # Leitura:
    palavra_chave = int(input("Digite o valor a procura: ").strip())
    # Processamento:
    banco_de_dados = [15, 20, 84, 73]
    x = 0
    while x < len(banco_de_dados):
        if banco_de_dados[x] == palavra_chave:
            print(f"{palavra_chave} achado na posição {x + 1}")
            break
        x += 1
    if palavra_chave not in banco_de_dados:
        print(f"{palavra_chave} não foi encontrado no banco de dados!")


if __name__ == "__main__":
    main()
