'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
maior_valor = None
menor_valor = None
lista = []
for c in range(5):
    valor = (int(input('Digite um número --> ')))
    lista.append(valor)
    if (maior_valor == None) and (menor_valor == None):
        maior_valor = valor
        menor_valor = valor
    elif valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor
print(f'O maior valor foi {maior_valor} no índice {lista.index(maior_valor)}')
print(f'O menor valor foi {menor_valor} no índice {lista.index(menor_valor)}')

