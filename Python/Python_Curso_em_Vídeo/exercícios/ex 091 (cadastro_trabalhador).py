'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
funcionario = {}
funcionario['nome'] = str(input('Digite o nome do funcionário: '))
funcionario['anonasc'] = int(input('Digite o ano de nascimento do funcionário: '))
funcionario['ctps'] = int(input("Digite a carteira de trabalho do funcionário: "))
if funcionario ['ctps'] != 0:
    funcionario['contratacao'] = int(input("Digite o ano de contratação do funcionário: "))
    funcionario['salario'] = str(input("Digite o salário do funcionário: "))

funcionario['idade'] = 2026 - funcionario['anonasc']
funcionario['aposentadoria'] = 65 - funcionario['idade']

print(f'{'-='*45}\nO nome do funcionário/a é --> {funcionario["nome"]}\nA idade do funcionário é --> {funcionario['idade']}')
if funcionario ['ctps'] != 0:
    print(f'O ano de contratação do funcionário/a é --> {funcionario["contratacao"]}\nO salário do funcionário é --> {funcionario["salario"]}\nA quantidade de anos que faltam para o funcionário/a se aposentar é --> {funcionario["aposentadoria"]}')