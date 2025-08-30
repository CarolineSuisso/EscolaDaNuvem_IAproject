def contador_par_impar():
    numeros_pares = 0
    numeros_impares = 0

    print("Digite números inteiros. Para finalizar e ver o resultado, digite 'fim'.")

    while True:
        entrada = input("Digite um número: ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"-> O número {numero} é PAR.")
                numeros_pares += 1
            else:
                print(f"-> O número {numero} é ÍMPAR.")
                numeros_impares += 1

        except ValueError:
            print("-> Entrada inválida. Por favor, insira apenas números inteiros.")

    
    print(f"Total de números PARES inseridos: {numeros_pares}")
    print(f"Total de números ÍMPARES inseridos: {numeros_impares}")

contador_par_impar()