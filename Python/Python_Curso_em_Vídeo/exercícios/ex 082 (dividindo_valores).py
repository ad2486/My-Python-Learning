'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = []
impares = []
while True:
    valor = input('Digite um valor ou digite [sair] para sair! -->  ')
    try:
        if valor.lower() == 'sair':
            break
        valint = int(valor)
        lista.append(valint)
        if valint % 2 == 0:
            pares.append(valint)
        else:
            impares.append(valint)
    except (TypeError, IndexError, ValueError):
        print('Digite um valor válido!')
    

print(f'Lista Geral --> {lista}')
print(f'Lista Pares --> {pares}')
print(f'Lista Ímpares --> {impares}')

