ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else: print(f"{ano} não é um ano bissexto.")
#a linha de código com ! significa 'Diferente de', ou seja se o ano for divisível por 4 e não for divisível por 100,
#ou se for divisível por 400, então é um ano bissexto. Caso contrário, não é um ano bissexto.