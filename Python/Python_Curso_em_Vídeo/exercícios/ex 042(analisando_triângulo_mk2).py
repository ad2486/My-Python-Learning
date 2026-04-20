l1 = float(input('Digite o primeiro lado do triângulo:'))
l2 = float(input('Digite o segundo lado do triângulo:'))
l3 = float(input('Digite o terceiro lado do triângulo:'))
if l1 == l2 == l3:
    print ('Seu triângulo é Equilátero, possiu todos os lados iguais!')
elif (l1 == l2 != l3) or (l1 != l2 == l3) or (l1 != l3 == l2):
    print ('Seu triângulo é Isósceles, possui dois lados iguais e um diferente!')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print ('Seu triângulo é Escaleno, possui todos os lados diferentes')
else:
    print ('Você digitou valores inválidos, não foi possível calcular!')
     
