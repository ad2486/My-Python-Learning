vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80: 
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
else: print('Tenha um bom dia! Dirija com segurança!')
if vel > 80:
    multa = (vel - 80)*7
    print(f'O valor da multa é de R${multa:.2f}')
