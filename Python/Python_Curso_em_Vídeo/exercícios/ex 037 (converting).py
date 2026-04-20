n = int(input('Digite um número: '))
print('Agora será decidida a base de conversão do número')
print('Digite 1 para binário, 2 para octal e 3 para hexadecimal!')
option = int(input("Digite sua escolha: "))

num = n  # guardar o número original

if option == 1:
    # BINÁRIO
    pot = 1
    while pot * 2 <= n:
        pot *= 2

    binario = ""
    while pot >= 1:
        if n >= pot:
            binario += "1"
            n -= pot
        else:
            binario += "0"
        pot //= 2

    print(f"O número {num} convertido em binário é: {binario}")

elif option == 2:
    # OCTAL
    pot = 1
    while pot * 8 <= n:
        pot *= 8

    octal = ""
    while pot >= 1:
        d = n // pot
        octal += str(d)
        n -= d * pot
        pot //= 8

    print(f"O número {num} em octal é: {octal}")

elif option == 3:
    # HEXADECIMAL
    pot = 1
    while pot * 16 <= n:
        pot *= 16

    hexa = ""
    hex_map = "0123456789ABCDEF"

    while pot >= 1:
        d = n // pot
        hexa += hex_map[d]
        n -= d * pot
        pot //= 16

    print(f"O número {num} em hexadecimal é: {hexa}")

else:
    print("Operação inválida!")
                                 
                        
    
      