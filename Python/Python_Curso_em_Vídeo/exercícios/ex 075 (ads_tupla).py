'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
v3 = int(input('Digite o terceiro valor:'))
v4 = int(input('Digite o quarto valor:'))

tupla = (v1, v2, v3, v4)
if 9 in tupla:
    print (f'O número 9 apareceu {tupla.count(9)} vezes!')

if 3 in tupla:
    print (f'O número 3 foi digitado pela primeira vez em {tupla.index(3) + 1}º lugar!')

for valor in tupla:
    if valor % 2 == 0:
        print (f'{valor} foi um dos números pares!') #eu queria é botar os valores numa lista e printar ela toda depois, mas o guanabara não tinha ensinado ainda, então evitei

        
        


       

