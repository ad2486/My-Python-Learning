'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                 
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                         
C) Se o valor 5 foi digitado e está ou não na lista.
'''
l = []
print('Digite (sair) para sair!')
while True:
    val = input('Digite um valor --> ').strip()
    try:
        valint = int(val)
        l.append(valint)
        if valint == 5:
            print('O valor 5 foi digitado!')
        l.sort(reverse=True)
        
    except (TypeError, ValueError):
        if val == 'sair':
            break
        else:
            print('Digite um valor válido!')
    
    
print(f'Foram digitados {len(l)} números!')
print(l)