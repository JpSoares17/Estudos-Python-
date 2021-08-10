def main():
    # Leitura:
    ultimoA = 10
    ultimoB = 10
    filaA = list(range(1, ultimoA + 1))
    filaB = list(range(1, ultimoB + 1))
    while True:
        print(f"\nExistem {len(filaA)} cliente(s) na fila A")
        print(f"\nExistem {len(filaB)} cliente(s) na fila B")
        print(f"Fila A: {filaA}")
        print(f"Fila B: {filaB}")
        print("Digite F para adicionar um cliente ao fim da fila A,")
        print("Digite G para adicionar um cliente ao fim da fila B,")
        print("ou A para realizar o atendimento na fila A,")
        print("ou B para realizar o atendimento na fila B. S para sair.")
        operacao = input("Operação (F, A ou S): ").upper()
        for comando in operacao:
            if comando == "A" and len(filaA) > 0:
                atendido = filaA.pop(0)
                print(f"Cliente {atendido} atendido na fila A")
            elif comando == "B" and len(filaB) > 0:
                atendido = filaB.pop(0)
                print(f"Cliente {atendido} atendido na fila B")
            elif comando == "A" and len(filaA) <= 0:
                print("Fila vazia! Ninguém para atender.")
            elif comando == "B" and len(filaB) <= 0:
                print("Fila vazia! Ninguém para atender.")
            elif comando == "F":
                ultimoA += 1
                filaA.append(ultimoA)
            elif comando == "G":
                ultimoB += 1
                filaB.append(ultimoB)
            elif comando == "S":
                continue
            else:
                print("Operação inválida! Digite apenas F, A ou S!")
        if operacao[-1] == "S":
            break


if __name__ == "__main__":
    main()
# Não posso substituir todos os while, pois nem todas as repetições tem um
# número limitado de repetições!
