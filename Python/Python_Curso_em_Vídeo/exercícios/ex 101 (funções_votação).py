'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(a):
    idade = 2026 - a
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    elif 18 <= idade < 70:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'

ano_nasc = int(input('Digite seu ano de nascimento: '))
print(f'{voto(ano_nasc)}')
