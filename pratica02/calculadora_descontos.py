produto = "camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * ( percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print (f"O valor da {produto} era de R${preco_original:.2f}, ocorreu um desconto de {percentual_desconto}%, onde o valor descontado foi de R${valor_desconto:.2f} e o valor total pago foi de R${preco_final:.2f}".replace('.' , ','))
