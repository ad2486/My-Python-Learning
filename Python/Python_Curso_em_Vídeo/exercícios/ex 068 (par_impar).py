'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import choice
lista = [1,2]
lista2 = ['par','impar']
contador = 0
while True:
    escolha_par_pc = choice(lista2)
    print (f'O computador escolheu {escolha_par_pc}')
    escolha_pc = choice(lista)
    escolha_jogador = int(input('Digite um número par ou ímpar:'))
    if escolha_par_pc == 'par':
        
        
        if (escolha_pc + escolha_jogador) % 2 == 0:
            print ('Você perdeu!')
            break
        
        
        else:
            contador = contador + 1
            print('Você ganhou!')
        
    
    if escolha_par_pc == 'impar':


        if (escolha_pc + escolha_jogador) % 2 != 0:
            print ('Você perdeu!')
            break


        else: 
            contador = contador + 1
            print('Você ganhou!')
            

print(f'Você venceu {contador} vezes!') 
