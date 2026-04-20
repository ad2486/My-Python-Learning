'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
h_velho = 0
nome_hv = ''
mulheres_menores = 0
soma_idade = 0
pessoas = []
for i in range(4):  
    nome = input('Digite o nome:').strip()
    idade = int(input('Digite a idade:'))
    sexo = input('Digite o sexo (M/F):').upper().strip()
    pessoa = {'nome': nome, 'idade': idade, 'sexo': sexo}
    pessoas.append(pessoa)
    
    
    #bloco de decisões do sexo masculino
    if sexo == 'M':
        if idade > h_velho:
            h_velho = idade
            nome_hv = nome

    
    #bloco de decisões do sexo feminino
    elif sexo == 'F':
        if idade < 20:
            mulheres_menores = mulheres_menores + 1
    
    soma_idade = soma_idade + idade
    

media_idade = soma_idade / 4

print(f'A média de idade do grupo é {media_idade}')
print(f'O nome do homem mais velho é {nome_hv}')
print(f'A quantidade de mulheres menores de 20 anos é {mulheres_menores}')

