def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0

    valor_da_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    return valor_da_gorjeta

conta_do_restaurante = 158.75
percentual_da_gorjeta = 15.0

gorjeta = calcular_gorjeta(conta_do_restaurante, percentual_da_gorjeta)

total_a_pagar = conta_do_restaurante + gorjeta

print(f"Valor da Conta: R$ {conta_do_restaurante:.2f}")
print(f"Porcentagem da Gorjeta: {percentual_da_gorjeta}%")
print("-" * 30)
print(f"Valor da Gorjeta: R$ {gorjeta:.2f}")
print(f"Valor Total a Pagar: R$ {total_a_pagar:.2f}")