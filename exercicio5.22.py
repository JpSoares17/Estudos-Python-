def main():
    # Leitura:
    while True:
        opcao = int(input('''
============== TABUADA ===============

    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    5 - Sair
======================================
Opção: ''').strip())
        # Processamento:
        numero_1 = 1
        numero_2 = 1
        if opcao == 1:
            while numero_1 <= 10:
                while numero_2 <= 10:
                    print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
                    numero_2 += 1
                numero_1 += 1
                numero_2 = 1
        if opcao == 2:
            while numero_1 <= 10:
                while numero_2 <= 10:
                    print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
                    numero_2 += 1
                numero_1 += 1
                numero_2 = 1
        if opcao == 3:
            while numero_1 <= 10:
                while numero_2 <= 10:
                    print(
                        f"{numero_1} / {numero_2} = {numero_1 / numero_2:.2f}")
                    numero_2 += 1
                numero_1 += 1
                numero_2 = 1
        if opcao == 4:
            while numero_1 <= 10:
                while numero_2 <= 10:
                    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
                    numero_2 += 1
                numero_1 += 1
                numero_2 = 1
        if opcao == 5:
            break


if __name__ == "__main__":
    main()
