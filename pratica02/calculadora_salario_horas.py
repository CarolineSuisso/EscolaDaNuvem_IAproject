numero_funcionarios = int(input("Número de funcionários: "))
quantidade_horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
valor_recebido_hora = int(input("Digite o valor recebido por hora:"))

salario = quantidade_horas_trabalhadas * valor_recebido_hora

print(f"Numer de funcionário/s = {numero_funcionarios}")
print(f"Salario = R$ {salario:.2f}") 
