'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou 
não na tela o processo de cálculo do fatorial.
'''
def fatorial(num, show=False):
    resultado = 1
    processo = ''
    for numero in range (num, 0, -1):
        resultado *= numero
        numero_string = str(numero)
        processo += numero_string + 'x'
    if show == False:
        return resultado
    elif show == True:
        print(f'O fatorial de {num} é: {resultado}')
        print(f'O processo do fatorial foi: {processo[:-1]}')
        return resultado        

fatorial(5, True)
        
