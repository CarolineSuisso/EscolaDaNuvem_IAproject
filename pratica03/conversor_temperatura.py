try:
    valor_temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Qual a unidade de origem? (C, F, K): ").upper()
    unidade_destino = input("Para qual unidade deseja converter? (C, F, K): ").upper()
except ValueError:
    print("Erro: O valor da temperatura deve ser um número.")
    exit()

resultado = 0

if unidade_origem == unidade_destino:
    resultado = valor_temperatura

elif unidade_origem == 'C':
    if unidade_destino == 'F':
        resultado = (valor_temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        resultado = valor_temperatura + 273.15
    else:
        print(f"Unidade de destino '{unidade_destino}' inválida.")
        exit()

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        resultado = (valor_temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        resultado = (valor_temperatura - 32) * 5/9 + 273.15
    else:
        print(f"Unidade de destino '{unidade_destino}' inválida.")
        exit()

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        resultado = valor_temperatura - 273.15
    elif unidade_destino == 'F':
        resultado = (valor_temperatura - 273.15) * 9/5 + 32
    else:
        print(f"Unidade de destino '{unidade_destino}' inválida.")
        exit()

else:
    print(f"Unidade de origem '{unidade_origem}' inválida.")
    exit()

print(f"{valor_temperatura}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")