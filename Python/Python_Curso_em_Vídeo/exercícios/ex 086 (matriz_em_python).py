'''
Exercício Python 086: Crie um programa que declare uma matriz 
de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [ [], [], []]
for c in range (9):
    matriz[c // 3].append(int(input('Digite um valor para a matriz: ')))

print(f'{ '-=' * 30}\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
