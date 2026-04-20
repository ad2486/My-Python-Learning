'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*val):
    maior = []
    for valor in val:
        if maior == []:
            maior.append(valor)
        elif maior != []:
            if valor > maior[0]:
                maior[0] = valor
    print(f'O maior valor é {maior[0]}')

        