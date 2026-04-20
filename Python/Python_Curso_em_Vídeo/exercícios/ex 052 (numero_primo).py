'''
Exercício Python 52: Faça um programa que leia um número 
inteiro e diga se ele é ou não um número primo.
'''
print ('Esse programa vai checar se o número é primo ou não!')
n = int(input('Digite o número que deseja checar:'))

e_primo = True
for i in range (2,n):
    if n % i == 0:
        print('Não é primo!')
        e_primo = False
        break
    
if e_primo:
    print('O número é primo!')

        