'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import choice
escolhas = [1,2,3,4,5,6]
jogadores = {}
jogadores['j_um'] = choice(escolhas)
jogadores['j_dois'] = choice(escolhas)
jogadores['j_tres'] = choice(escolhas)
jogadores['j_quatro'] = choice(escolhas)
jogadores_f = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
# sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
print (jogadores_f)