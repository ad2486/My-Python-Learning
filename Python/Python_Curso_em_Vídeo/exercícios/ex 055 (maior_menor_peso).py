'''
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
'''
# Lê o primeiro peso e já define maior e menor
peso = float(input('Digite seu peso: '))
maior_peso = peso
menor_peso = peso

# Agora lê os outros 4 pesos
for i in range(4):
    peso = float(input('Digite seu peso: '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é {maior_peso}!')
print(f'O menor peso é {menor_peso}!')

