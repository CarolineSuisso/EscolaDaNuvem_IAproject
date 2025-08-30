def calculadora():
    
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print(f"O resultado é: {resultado}")
            break

        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")

calculadora()