
from random import choice
print ('Bem vindo ao jogo da adivinhação!')
número = int(input('Digite um número entre 1 e 5: '))
lista = [1,2,3,4,5]
ne = choice(lista)
if número == ne:
    print('Parabéns! Você acertou!')
else: print('Que pena! Você errou! O número era {}'.format(ne))
2