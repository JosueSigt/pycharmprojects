'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade 
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
largura = float(input('Largura da parede: '))
altura = float(input('Altura de parede: '))
área = largura * altura
print(f'Sua parede tem a dimensão de {largura:2} x {altura:2} e sua área é de {área}m².')
tinta = área/2
print(f'Para pintar essa parede você precisará de {tinta}l de tinta')


