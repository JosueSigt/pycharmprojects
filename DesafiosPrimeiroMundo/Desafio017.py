'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem seno de {seno:.2f}')
cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O âgulo de {ângulo} tem a tangente de {tangente:.2f}')