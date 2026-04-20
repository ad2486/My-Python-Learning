a = int(input('Digite seu ano de nascimento:'))
i = 2026 - a
if i <= 9:
    print('Mirim')
elif i <= 14:
    print('Infantil')
elif i <= 19:
    print('Junior')
elif i <= 20:
    print('Sênior')
else:
    print('Master')