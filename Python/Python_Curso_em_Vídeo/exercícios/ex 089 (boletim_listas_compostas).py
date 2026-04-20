'''
Exercício Python 089: Crie um programa que leia nome e duas notas de 
vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e 
permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
geral = []
notas = []
alunos = int(input('Quantos alunos você deseja cadastrar?\n--> '))
for c in range (alunos):
    aluno = []
    nota = []
    aluno.append(input('Digite o nome do aluno\n--> '))
    n1 = float(input('Digite a primeira nota do aluno\n--> '))
    n2 = float(input('Digite a segunda nota do aluno\n--> '))
    nota.append(n1)
    nota.append(n2)
    media = (n1+n2)/2
    aluno.append(media)
    geral.append(aluno)
    notas.append(nota)
    

decisao = input('Deseja ver os alunos cadastrados? (S/N)\n--> ').upper().strip()
if decisao == 'S':
    print(f'{'-='*30}\n{'Nº':<20} {'Nome':^20} {'Média':>20}\n{'-'*60}')
    for aluno in geral:
        print(f'{geral.index(aluno):<20} {aluno[0]:^20} {aluno[1]:>20}')
    decisao_dois = input('Deseja ver as notas de um aluno específico? (S/N)\n--> ').upper().strip()
    if decisao_dois == 'S':
        nota_aluno = int(input('Digite o número do aluno correspondente no boletim para ver sua nota\n--> '))
        print(f'As notas de {geral[nota_aluno][0]}, foram\n--> {notas[nota_aluno]}')
else:
    print('O programa será encerrado!')
        

