''' Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
possíveis sobre ela'''
# algo
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmérico? ', a.isalnum())
print('Está em mauiscúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
