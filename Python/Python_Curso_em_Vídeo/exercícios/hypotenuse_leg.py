from math import sqrt
co = float (input('Digite o cateto oposto'))
ca = float (input('Digite o cateto adjacente'))
hi = pow(co, 2)+pow(ca, 2)
print (f'A hipotenusa desse triângulo retângulo é {sqrt(hi):.2f}')
