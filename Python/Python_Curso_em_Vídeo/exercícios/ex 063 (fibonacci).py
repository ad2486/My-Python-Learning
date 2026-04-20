n = int(input('Digite quantos valores de uma sequência de Fibonacci você deseja ver:'))
a = 0
b = 1
while n > 0:
    print (a)
    proximo = a + b
    a = b 
    b = proximo
    n = n - 1


