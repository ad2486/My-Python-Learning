anonasc = int(input('Qual o ano em que você nasceu?'))
idade = 2026 - anonasc 
if idade < 18:
    print(f'Você ainda vai se alistar, espere {18-idade} ano/s!')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Você já passou do tempo do alistamento, está {idade-18} ano/s atrasado!')