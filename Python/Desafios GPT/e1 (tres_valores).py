v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
if v1 > v2 and v1 > v3:
    print('O primeiro valor é o maior valor.')
elif v2 > v1 and v2 > v3:
    print('O segundo valor é o maior valor.')
elif v3 > v1 and v3 > v2:
    print('O terceiro valor é o maior valor.')
elif v1 == v2 == v3:
    print('Os três valores são iguais.')
elif v1 == v2 and v1 > v3:
    print('O primeiro e o segundo valor são iguais e maiores que o terceiro valor.')
elif v2 == v3 and v2 > v1:
    print ('O segundo e o terceiro valor são iguais e maiores que o primeiro valor.')
elif v1 == v3 and v1 > v2: 
    print ('O primeiro e o terceiro valor são iguais e maiores que o segundo valor.')

#Chat deu outra solução mais simples, mas com o mesmo resultado de acordo com ele:
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

maior = max(v1, v2, v3)

print(f'O maior valor é {maior}')