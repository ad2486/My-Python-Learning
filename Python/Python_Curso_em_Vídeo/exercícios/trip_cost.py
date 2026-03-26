d = int(input('Digite a distância da viagem em km: '))
if d <= 200:
    custo = d * 0.50
    print ('O custo da viagem é R$ {:.2f}'.format(custo))
else:   custo = d * 0.45
print (f'O custo da viagem é R$ {custo:.2f}')

