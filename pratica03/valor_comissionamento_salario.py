try:
    nome_vendedor = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
    total_vendas = float(input("Digite o total de vendas efetuadas no mês: R$ "))

    comissao = total_vendas * 0.15
    total_a_receber = salario_fixo + comissao

    print(f"TOTAL = R$ {total_a_receber:.2f}")

except ValueError:
    print("Erro: Os valores de salário e vendas devem ser numéricos.")