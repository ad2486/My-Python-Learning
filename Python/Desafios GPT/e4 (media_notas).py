n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'A média é {media:.2f}. Aluno aprovado!')
elif media >= 5:
    print(f'A média é {media:.2f}, Aluno em recuperação.')
else: 
    print(f'A média é {media:.2f}. Aluno reprovado!')