'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
#moeda.py
def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
def aumentar(valor=0, porcentagem=100, format=False):
    res = valor + (valor * (porcentagem/100))
    if not format:
        return res
    if format:
        return moeda(res)
def diminuir(valor=0, porcentagem=100, format=False):
    res = valor - (valor * (porcentagem/100))
    if not format:
        return res
    if format:
        return moeda(res)
def dobro(valor=0, format=False):
    res = valor * 2
    if not format:
        return res
    if format:
        return moeda(res)
def metade(valor=0, format=False):
    res = valor / 2
    if not format:
        return res
    if format:
        return moeda(res)