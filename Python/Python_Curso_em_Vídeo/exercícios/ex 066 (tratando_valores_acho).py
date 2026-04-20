'''
Exercício Python 66: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
valores = []
c = False
while not c:
    valor = int(input('Digite um valor:'))
    if valor == 999:
        break
    else:
        valores.append(valor)

print(f'A soma dos valores é: {sum(valores)}')
    