'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

produto_mais_barato = ''
preco_mais_barato = None
total_gasto = 0
mais_de_mil = 0

while True:

    #bloco de entrada
    nome = input('Digite o nome do produto:').strip()
    preco = float(input('Digite o preço do produto:'))

    #Variável pra printar no final
    total_gasto += preco

    #Contador pra produtos com preço > 1000
    if preco > 1000:
        mais_de_mil += 1
    
    #Filtração pra ver qual o nome do produto mais barato
    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    #Bloco de decisão de continuidade do usuário
    while True:
        continuar = input('Deseja continuar (S/N)? ').upper().strip()
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
        else:
            print('Digite um valor válido!')

    if continuar == 'N':
        break    

print(f'O produto mais barato é {produto_mais_barato}!')
print(f'O total gasto foi {total_gasto:.2f} R$!')
print(f'{mais_de_mil} produtos custaram mais de 1000 Reais!')    