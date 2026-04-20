'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:                                                                                                   
A) Quantas pessoas foram cadastradas.                                                                                                               
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
'''
c_pessoas = 0
pessoas = []
while True:
    
    s_n = input('Deseja adicionar uma pessoa? (S/N) --> ').upper()
    
    if s_n == 'S':
        nome = input('Digite o nome --> ')
        peso = int(input('Digite o peso --> '))
        c_pessoas += 1
        pessoas.append([nome, peso])
    
    elif s_n == 'N':
        break
    
    else:
        print('Digite uma opção válida!')

mais_pesadas = max(pessoas, key=lambda pessoa: pessoa[1])
mais_leves = min(pessoas, key=lambda pessoa: pessoa[1])
print(f'Foram cadastradas {c_pessoas} pessoas!')
print(f'O mais pesado foi {mais_pesadas}')
print(f'O mais leve foi {mais_leves}')    

