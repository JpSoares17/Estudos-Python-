def main():
    # Leitura:
    ultimo = 10
    fila = list(range(1, ultimo + 1))
    while True:
        print(f"\nExistem {len(fila)} cliente(s) na fila")
        print(f"Fila atual: {fila}")
        print("Digite F para adicionar um cliente ao fim da fila,")
        print("ou A para realizar o atendimento. S para sair.")
        operacao = input("Operação (F, A ou S): ").upper()
        for comando in operacao:
            if comando == "A" and len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            elif comando == "A" and len(fila) <= 0:
                print("Fila vazia! Ninguém para atender.")
            elif comando == "F":
                ultimo += 1
                fila.append(ultimo)
            elif comando == "S":
                continue
            else:
                print("Operação inválida! Digite apenas F, A ou S!")
        if operacao[-1] == "S":
            break


if __name__ == "__main__":
    main()
