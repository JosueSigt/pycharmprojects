# Escreva um que leia um valor em metros e o exiba convertido em quilômetros, Hectômetro, Decâmetro, decímetro, centímetros e milímetros
metros = float(input('Digite um valor em metros: '))
quilometros = metros/1000
hecatometros = metros/100
decatometros = metros/10
decimetros = metros*10
centimetros = metros*100
milimetros = metros*1000

print('O valor em quilometros é: ', quilometros)
print('O valor em hecatometro é: ', hecatometros)
print('O valor em decametros é: ', decatometros)
print('O valor em decimetros é: ', decimetros)
print('O valor em centimetros é: ', centimetros)
print('O valor em milimetros é: ', milimetros)
