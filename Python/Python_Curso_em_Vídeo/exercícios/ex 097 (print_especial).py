'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
Ex:                                                                                                                                                                        
escreva(‘Olá, Mundo!’) Saída:                                                                                                                          
~~~~~~~~~                                                                                                                                                            
Olá, Mundo!                                                                                                                                                          
~~~~~~~~~            
'''
def escreva(a):
    print(f'{'~'* (len(a)+2)}')
    print(f'{a:^{len(a) + 2}}')
    print(f'{'~'* (len(a)+2)}')

escreva('Olá, Bem Vindo!')