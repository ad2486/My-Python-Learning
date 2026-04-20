'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

valor = int(input('Digite quanto você deseja sacar em R$: '))

notas_cinquenta = valor // 50
valor %= 50

notas_vinte = valor // 20
valor %= 20

notas_dez = valor // 10
valor %= 10

notas_um = valor

print(f'Notas de R$50: {notas_cinquenta}')
print(f'Notas de R$20: {notas_vinte}')
print(f'Notas de R$10: {notas_dez}')
print(f'Notas de R$1: {notas_um}')


