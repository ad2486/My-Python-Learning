v = float(input('Digite o valor da casa que deseja comprar:'))
s = float(input('Digite seu Salário:'))
a = float(input('Digite em quantos anos você deseja pagar:'))
ts = s*0.3
m = a*12
pm = v/m
if pm > ts:
    print('Empréstimo negado, prestação muito alta!')
else:
    print('Empréstimo permitido, a transferência será efetivada!')