'''
Exercício Python 060: Faça um programa que leia 
um número qualquer e mostre o seu fatorial.
'''
n = int(input('Digite o número que deseja ver o fatorial:'))
v = 1
while n > 1:
    v = v*n
    n = n - 1 
print (v)


        
    