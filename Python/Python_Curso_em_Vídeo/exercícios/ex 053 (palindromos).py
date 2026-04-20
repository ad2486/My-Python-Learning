'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''
frase = input('Digite a frase desejada').lower().strip()
frase_semespacos = frase.replace(' ', '')
frase_invertida = frase_semespacos[::-1]
if frase_invertida == frase_semespacos:
    print('Sua frase é um Palíndromo!')
else:
    print('Sua frase não é um Palíndromo!')