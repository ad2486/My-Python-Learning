from random import choice
numeros = [0,1,2,3,4,5,6,7,8,9,10]
acertou = False
contador = 0
while not acertou:
    chute = int(input('Tente adivinhar o número:'))
    computador = choice(numeros)
    if chute == computador:
        contador += 1
        print(f'Você acertou! Precisou de {contador} tentativas!')
        break
    else:
        contador += 1
        print('Você errou, tente de novo!')