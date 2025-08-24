peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:" ))

imc = peso / (altura ** 2)

if imc <= 18.5: 
    print(f"Seu IMC é:{imc:.2f}")
    print("Classficação: Abaixo do peso")

elif imc < 25:
    print(f"Seu IMC é:{imc:.2f}")
    print("Classificação: Peso normal.")

elif imc < 30:
    print(f"Seu IMC é:{imc:.2f}")
    print("Classificação: Sobrepeso.")
    
elif  imc < 35:
    print(f"Seu IMC é:{imc:.2f}")
    print("Classificação: Obesidade Grau I.")

elif imc < 40:
    print(f"Seu IMC é:{imc:.2f}")
    print("Classificação: Obesidade Grau II.")

else:
    print(f"Seu IMC é:{imc:.2f}")
    print("Classificação: Obesidade Grau III.")