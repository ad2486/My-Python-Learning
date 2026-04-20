'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre 
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
valores = []
while True:
    valor = int(input('Digite um valor:'))
    valores.append(valor)

    media = sum(valores) / len(valores)
    maior = max(valores)
    menor = min(valores)

    print(f'A média entre os valores é {media:.2f}')
    print(f'O maior valor é {maior}')
    print(f'O menor valor é {menor}')

    continuar = input('Deseja continuar (S/N)?').upper().strip()
    if continuar == 'N':
        break