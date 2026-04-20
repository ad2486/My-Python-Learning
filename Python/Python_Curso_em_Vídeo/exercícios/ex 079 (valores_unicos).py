'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista = []
digitar = int(input('Quantos valores você deseja digitar? --> '))
for c in range (digitar):
    valor = int(input('Digite um valor --> '))
    if valor not in lista:
        lista.append(valor)
        
    else:
        print('Valores repitidos serão ignorados!')

lista.sort()
print (lista)