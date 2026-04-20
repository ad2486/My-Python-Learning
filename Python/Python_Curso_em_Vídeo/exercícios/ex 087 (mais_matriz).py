'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
'''
matriz = [ [], [], []]
pares = []
for c in range (9):
    valor = int(input('Digite um valor para a matriz: '))
    matriz[c // 3].append(valor)
    if valor % 2 == 0:
        pares.append(valor)
soma_coluna = []
for ad in range(3):
    coluna = (matriz[ad][2])
    
    soma_coluna.append(coluna)

print(f'{ '-=' * 30}\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma de todos os valores pares digitados é: {sum(pares)}')
print(f'A soma de todos valores da terceira coluna é: {sum(soma_coluna)}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')