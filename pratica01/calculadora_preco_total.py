"""4- Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""


produto = "cadeira"
preco_unidade = 12.40
quantidade = 3
valor = preco_unidade * quantidade

#f"...."" usado para upar a string de forma mais facil usando {} e o 2f formata a variavel
print(f"---Detalhes da compra---")
print(f"Nome do produto: {produto}")
print(f"Preço unitário: R$ {preco_unidade:.2f}".replace('.', ','))
print(f"Quantidade:{quantidade}")
print("---------------")


print(f"O preço total da compra é de R${valor}".replace('.',','))