

valor_real = 100
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolares = valor_real / taxa_dolar
valor_euros = valor_real / taxa_euro

valor_dolares_arredondado = round(valor_dolares, 2)
valor_euros_arredondado = round(valor_euros, 2)

print (f"O valor de R$ {valor_real:.2f} corresponde a:")
print(f"US${valor_dolares_arredondado}")
print(f"£{valor_euros_arredondado}")







