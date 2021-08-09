def main():
    # Processamento:
    abertura = []
    while True:
        # Leitura aninhada:
        texto = input("Digite o cojunto de parenteses: ").strip()
        for parentese in texto:
            if parentese == "(":
                abertura.append(parentese)
            elif parentese == ")":
                del abertura[-1]
            else:
                print("Caractere inválido! Próximo...")
        if len(abertura) == 0:
            print("OK!")
        else:
            print("Erro!")


if __name__ == "__main__":
    main()
