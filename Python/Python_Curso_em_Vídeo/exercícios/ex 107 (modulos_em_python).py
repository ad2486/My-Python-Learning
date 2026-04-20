#moeda.py
'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
def aumentar(valor, porcentagem):
    return valor + (valor * (porcentagem/100))
def diminuir(valor, porcentagem):
    return valor - (valor * (porcentagem/100))
def dobro(valor):
    return valor * 2
def metade(valor):
    return valor / 2