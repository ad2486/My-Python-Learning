'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
def sorteia():
    from random import randint
    sorteados = []
    for c in range (5):
        valor = randint(1,10000)
        sorteados.append(valor)
    return sorteados

def somaPar(*val):
    soma = 0
    for valor in val:
        if valor % 2 == 0:
            soma += valor
    print (soma)

somaPar(*sorteia())

        
    