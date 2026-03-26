from math import radians, sin, cos, tan
a = float(input('Digite o ângulo desejado:'))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print (f'O seno é {seno:.2f}\nO cosseno é {cos:.2f}\nA tangente é {tan:.2f}')
