from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    try:
        data_hoje = date.today()

        if ano_nascimento > data_hoje.year:
            print("Erro: O ano de nascimento não pode ser no futuro.")
            return 0

        data_nascimento = date(ano_nascimento, 1, 1)
        
        diferenca = data_hoje - data_nascimento
        
        return diferenca.days
        
    except (ValueError, TypeError):
        print("Erro: O ano informado é inválido.")
        return 0

print("--- Calculadora de Idade em Dias ---")

while True:
    try:
        ano_input = int(input("Digite o seu ano de nascimento (ex: 1995): "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas o ano com números.")

idade_dias = calcular_idade_em_dias(ano_input)

if idade_dias > 0:
    print(f"\nDesde o início do ano de {ano_input}, já se passaram {idade_dias:,} dias.")