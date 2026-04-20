'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''
mulheres = []
idades = []
pessoas = []
acima_media = []

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Digite o nome da pessoa: ')).capitalize().strip()
    pessoa['sexo'] = str(input('Digite o sexo da pessoa (M/F): ')).upper().strip()
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(pessoa)
    idades.append(pessoa['idade'])
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)
    op = str(input('Deseja continuar? (S/N): ')).upper().strip()
    if op == 'S':
        continue
    elif op == 'N':
        break

media = sum(idades) / len(idades)
for p in pessoas:
    if p['idade'] > media:
        acima_media.append(p)

print(f'{'-='*45}\nA) => Ao todo temos {len(pessoas)} cadastradas!\nB) => A média de idade é {media:.2f}\nC) => As mulheres são:\n{mulheres}\nD) => As pessoas com idade acima da média são:\n{acima_media}')


