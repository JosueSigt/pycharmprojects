'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

número = int(input('\033[30mMe diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')