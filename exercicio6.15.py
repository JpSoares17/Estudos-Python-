def main():
    # Processamento:
    lista = [3, 3, 1, 5, 4]
    fim = len(lista)
    while fim > 1:
        trocou = False
        indice = 0
        while indice < (fim - 1):
            if lista[indice] > lista[indice + 1]:
                trocou = True
                temporario = lista[indice]
                lista[indice] = lista[indice + 1]
                lista[indice + 1] = temporario
            indice += 1
        if not trocou:
            break
        fim -= 1
    for ordenado in lista:
        print(ordenado)


if __name__ == "__main__":
    main()
