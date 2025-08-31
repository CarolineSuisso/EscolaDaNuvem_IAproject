def calcular_preco_final():
    print("--- Calculadora de Preço com Desconto ---")

    while True:
        try:
            preco_original = float(input("Digite o preço original do produto (ex: 250.75): R$ "))
            percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

            if preco_original < 0 or percentual_desconto < 0:
                print("\nErro: O preço e o desconto não podem ser valores negativos. Tente novamente.\n")
                continue

            break

        except ValueError:
            print("\nErro: Entrada inválida. Por favor, digite apenas números.\n")

    valor_do_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_do_desconto

    print("\n--- Resumo do Cálculo ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto de {percentual_desconto}%: R$ {valor_do_desconto:.2f}")
    print("-" * 25)
    print(f"Preço Final: R$ {preco_final:.2f}")

calcular_preco_final()