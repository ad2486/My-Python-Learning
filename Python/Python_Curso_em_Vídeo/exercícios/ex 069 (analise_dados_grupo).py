'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

c_homens = 0
c_mulheres_menores = 0
c_mais_dezoito = 0

while True:
    idade = int(input('Digite a idade:'))
    sexo = (input('Digite o sexo (M/F):')).upper().strip()

    
    if sexo == 'M':
        c_homens += 1
    if idade > 18:
        c_mais_dezoito += 1
    
    elif sexo == 'F':
        if idade > 18:
            c_mais_dezoito += 1
        if idade < 20:
            c_mulheres_menores += 1
    
    else: 
        print('Digite um sexo válido!')
    
    continua = input('Deseja continuar (S/N)?').upper().strip()

    if continua == 'N':
        break
    elif continua == 'S':
        continue
    else:
        print('Digite um valor válido!')


print(f'{c_mais_dezoito} pessoas tem mais de 18 anos!')
print(f'{c_homens} homens foram cadastrados!')
print(f'{c_mulheres_menores} mulheres tem menos de 20 anos!')
    
    


