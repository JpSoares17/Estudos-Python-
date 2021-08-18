def main():
    # Leitura:
    baixa = input("Digite o produto retirado: ").strip()
    quantidade = int(input("Digite a quantidade retirada: ").strip())
    # Processamento:
    estoque = {"tomate": [1000, 2.30],
               "alface": [500, 0.45],
               "batata": [2001, 1.20],
               "feijao": [100, 1.50]}
    if baixa in estoque and quantidade <= estoque[baixa][0]:
        estoque[baixa][0] -= quantidade
    elif baixa in estoque and quantidade > estoque[baixa][0]:
        print(f"Temos apenas {estoque[baixa][0]} de {baixa} no estoque!")
        estoque[baixa][0] = 0
    else:
        print(f"Não temos {baixa} no estoque!")
    # Saída:
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")


if __name__ == "__main__":
    main()
