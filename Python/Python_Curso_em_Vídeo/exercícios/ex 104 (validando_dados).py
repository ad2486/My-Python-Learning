'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaInt(val='<sem mensagem>'):
    while True:
        valor = input(f'{val}')
        try:
            int(valor)
            print('O valor é inteiro!')
            return int(valor)
        except:
            print('Digite um valor inteiro!')
    
leiaInt()


        


    