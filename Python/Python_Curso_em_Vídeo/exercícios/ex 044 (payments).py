v = float(input('Digite o valor do produto:'))
print('Agora você vai escolher o método de pagamento, Temos: à vista, à vista no cartão, em até 2x no cartão e 3x ou mais!')
print ('Digite, vista, vistac, 2x ou 3x para os métodos, respectivamente.')
mp = input('Qual o método de pagamento preferível?').strip()
if mp.lower() == 'vista':
    print (f'O valor a ser pago é {v-(0.1*v)}, você tem 10% de desconto!!')
elif mp.lower() == 'vistac':
    print (f'O valor a ser pago é {v-(0.05*v)}, você tem 5% de desconto!')
elif mp.lower() == '2x':
    print (f'O valor a ser pago é {v}, você paga o preço cheio!')
elif mp.lower() == '3x':
    print (f'O valor a ser pago é {v+(0.2*v)}, você tem 20% de juros extra!')
else:
    print ('Você não digitou um método de pagamento válido, por favor tente de novo!')