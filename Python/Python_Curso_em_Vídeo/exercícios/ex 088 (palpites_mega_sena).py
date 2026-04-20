'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''

from random import randint
gerados = int(input('Quantos jogos deseja gerar?\n--> '))
jogadas = [] 
for c in range (gerados):
    jogada = []
    for a in range (6):
        valor = randint(1,60)
        jogada.append(valor)
    jogadas.append(jogada)

print(jogadas)




