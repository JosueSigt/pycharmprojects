#Faça um program em pythom que calcule o valor gasto em combustível em uma viagem
'''Calcule o valor gasto em combustível em uma viagem, 
considerando o preço do combustível por litro, a distância percorrida e o consumo médio do veículo.'''
def calcular_gasto_combustivel(distancia, consumo_medio, preco_combustivel):
    litros_consumidos = distancia / consumo_medio
    valor_gasto = litros_consumidos * preco_combustivel
    return valor_gasto

# Entrada de dados pelo usuário
distancia = float(input("Digite a distância percorrida em quilômetros: "))
consumo_medio = float(input("Digite o consumo médio do veículo em km/l: "))
preco_combustivel = float(input("Digite o preço do combustível por litro: "))

# Chamada da função para calcular o gasto
gasto_combustivel = calcular_gasto_combustivel(distancia, consumo_medio, preco_combustivel)

# Exibindo o resultado
print("O valor gasto em combustível será de R$ {:.2f}".format(gasto_combustivel))
