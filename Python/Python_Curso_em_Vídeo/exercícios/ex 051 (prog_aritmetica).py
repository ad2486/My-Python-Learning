'''
Exercício Python 51: Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.
'''
primero_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

termo = primeiro_termo

for i in range (11):
    print (termo)
    termo = termo + razao
