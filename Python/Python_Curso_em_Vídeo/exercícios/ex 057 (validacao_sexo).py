certo = False
while not certo:
    sexo = input('Digite seu sexo (M/F):').upper().strip()
    if sexo == 'M':
        certo = True
        print('Informação Guardada!')
    elif sexo == 'F':
        print('Informação Guardada')
    else:
        print('Sexo não válido, tente de novo!') 