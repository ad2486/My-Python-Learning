'''
Exercício Python 51: Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.

primero_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

termo = primeiro_termo

for i in range (11):
    print (termo)
    termo = termo + razao
'''


primeiro_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
contador = 10
termo = primeiro_termo


while contador > 1:
    print (termo)
    termo += razao
    contador -= 1