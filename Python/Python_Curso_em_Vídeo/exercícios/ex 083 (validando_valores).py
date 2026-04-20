'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
'''
exp = input('Digite a expressão --> ').strip()
parenteses_abertos = exp.count('(')
parenteses_fechados = exp.count(')')
if parenteses_abertos == parenteses_fechados:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
'''
lista = []
exp = input('Digite a expressão --> ').strip()
for caractere in exp:
    if '(' in caractere:
        lista.append(1)
    elif ')' in caractere:
        if lista != []:
                lista.pop()

if lista == []:
    print ('Expressão Válida!')
else:
    print ('Expressão Inválida!')
    