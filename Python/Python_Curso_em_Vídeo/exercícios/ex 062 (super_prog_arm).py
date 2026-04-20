'''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

primeiro_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
contador = 10
termo = primeiro_termo


while contador >= 1:
    print (termo)
    if contador == 1:
        contador = int(input(('Você deseja mostrar mais alguns termos? Se sim digite um valor maior que 0, se não digite 0:')))
    termo += razao
    contador -= 1
    

