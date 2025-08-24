Idade = int(input("Digite sua idade:"))

if Idade >=0 and Idade <= 12:
    print("Classificação: Criança.")

elif Idade >=13 and Idade <= 17:
    print("Classificação: Adolescente.")

elif Idade >=18 and Idade <= 59:
    print("Classificação: Adulto.")

else:
    print("Classificação: Idoso.")