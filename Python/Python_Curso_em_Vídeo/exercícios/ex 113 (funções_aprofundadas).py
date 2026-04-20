'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
from cores import *
def leiaInt():
    while True:
        try:
            entrada = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'{VERMELHO}ERRO: por favor, digite um número inteiro válido{RESET}')
        else:
            return entrada


def leiaFloat():
    while True:
        try:
            entrada = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'{VERMELHO}ERRO: por favor, digite um número real válido{RESET}')
        else:
            return entrada
            

leiaInt()
leiaFloat()