idades = [13,15,18,30,50,75,90,79,5,10,94,24,35,60,62,70]
for idade in idades:
    if idade >= 60:
        print(f'{idade} anos: Idoso')
    elif idade >= 18:
        print(f'{idade} anos: Adulto')
    else:
        print(f'{idade} anos: Criança')

'''for é um loop que pega um valor por lista da vez e coloca dentro da variável idade, o if verifica se a idade é maior ou igual a 18,
se for, entra no if, no else, se não for maior ou igual a 18 ele entra no else.'''
