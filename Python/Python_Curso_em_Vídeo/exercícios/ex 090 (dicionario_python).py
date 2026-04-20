'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''
lista = []
while True:
    boletim = {}
    boletim['nome'] = str(input("Digite o nome do aluno: "))
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    boletim['media'] = (n1+n2)/2

    lista.append(boletim)

    op = str(input("Deseja continuar? (S/N): "))
    if op == "S":
        continue
    elif op == "N":
        break
    else:
        print("Digite apenas S/N!")
op_dois = str(input("Deseja mostrar o boletim? (S/N): "))
if op_dois == "S":
    print(f'{"-="*30}')
    print(f'{"Boletim":^60}')
    for b in lista:
        print(f"{str(b):^60}")
        
