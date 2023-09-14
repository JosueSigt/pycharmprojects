'''Faça um programa que leia um número inteiro e mostre o seu sucessor e o seu antecessor'''
n = int(input('Digite um número: '))
def new_func(n):
    print(f'Analisando o valor {n}, o seu antecessor é {n-1}, e o seu sucessor é {n+1},')

new_func(n)
