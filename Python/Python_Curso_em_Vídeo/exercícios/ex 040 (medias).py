n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m < 5.0:
    print(f'Sua média é {m}, Reprovado!')
elif 5.0 < m < 6.9:
    print(f'Sua média é {m}, Recuperação!')
elif m >= 7.0:
    print(f'Sua média é {m}, Aprovado!')
else:
    print('Não foi possível calcular a média')

