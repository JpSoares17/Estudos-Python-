def main():
    # Processamento:
    banco_de_dados = [1, 7, 2, 4]
    maximo = banco_de_dados[0]
    minimo = banco_de_dados[0]
    for numero in banco_de_dados:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    print(" Max | Min ")
    print( f"  {maximo}  |  {minimo}  ")


if __name__ == "__main__":
    main()
