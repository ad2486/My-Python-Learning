'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
maiores = 0
menores = 0
for i in range (7):
    anonasc = int(input('Digite seu ano de nascimento:'))
    if anonasc >= 2008:
        menores = menores + 1
    elif anonasc < 2008:
        maiores = maiores + 1
print (f'O número de maiores de idade é {maiores}')
print (f'O número de menores de idade é {menores}')
    