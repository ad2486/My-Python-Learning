'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
lista = []
for c in range (5):
    val = int(input('Digite um valor --> '))
    if lista == []:
        lista.append(val)
    else:
        for c, valor in enumerate(lista):
            if val < valor:
                lista.insert(c,val)
                break
        else:
            lista.append(val)
print(lista)