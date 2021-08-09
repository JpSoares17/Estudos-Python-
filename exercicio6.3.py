def leitura():
    lista = []
    while True:
        item = int(input("Digite o(s) item da lista: ").strip())
        if item == 0:
            break
        lista.append(item)
    return lista


def main():
    # Leitura:
    lista_1 = leitura()
    lista_2 = leitura()
    # Processamento:
    for item in lista_2:
        if item not in lista_1:
            lista_1.append(item)
    # Saída:
    print(lista_1)


if __name__ == "__main__":
    main()
