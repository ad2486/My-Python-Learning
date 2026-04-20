'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    
    n = int(input('Qual número você deseja ver a tabuada?'))
    
    
    if n < 0:
        break
    
    
    for c in range(1,11):
        print(n * c)

   