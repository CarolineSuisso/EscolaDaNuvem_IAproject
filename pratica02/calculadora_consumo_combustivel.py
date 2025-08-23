distancia_percorrida = 300 
combustivel_gasto = 25

consumo = distancia_percorrida / combustivel_gasto
consumo_arredondado = round(consumo, 2)

print("Relatóro de consumo")
print("--------------------")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto no trajeto: {combustivel_gasto} litros.")

print(f"Consumo médio: {consumo_arredondado} km/lt.")

