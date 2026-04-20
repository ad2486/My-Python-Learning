'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
# I think its better to ask for the numbers one time before the loop so you don't need to use option 4 every time you start the program

while True:
    print('Escolha uma das seguintes opções:')
    sleep(1)
    opcoes = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n-->'))
    
    if opcoes == 1:
        sleep(1)
        print('A soma de {} e {} resulta em: {}'.format(n1,n2, n1 + n2))
    
    elif opcoes == 2:
        sleep(1)
        print('O produto de {} e {} resulta em: {}'.format(n1,n2, n1 * n2))
    
    elif opcoes == 3:
        sleep(1)
        if n1 > n2:
            sleep(1)
            print('{} é o maior número!'.format(n1))
        elif n2 > n1:
            sleep(1)
            print('{} é o maior número!'.format(n2))
        elif n1 == n2:
            sleep(1)
            print('Os números são iguais!')
    
    elif opcoes == 4:
        sleep(1)
        n1 = int(input('Digite o primeiro número:'))
        sleep(1)
        n2 = int(input('Digite o segundo número:'))
        sleep(1)
        print (f'Os números foram atualizados para {n1} e {n2}!')
    
    elif opcoes == 5:
        sleep(1)
        print('Obrigado por usar o programa!')
        sleep(1)
        break
    
    else:
        sleep(1)
        print('Por favor digite um valor válido!')





# I'm using format in the odd way just to remember, bc my teacher was teaching with .format() in an old python version