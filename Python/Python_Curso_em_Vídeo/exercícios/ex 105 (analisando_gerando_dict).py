'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas 
de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)
'''
def notas(*nota, sit=False):
    q_notas = []
    dicionario = {}
    for n in nota:
        q_notas.append(n)
    dicionario['quantidade de notas'] = len(q_notas)
    dicionario['maior nota'] = max(q_notas)
    dicionario['menor nota'] = min(q_notas)
    media = sum(q_notas)/len(q_notas)
    dicionario['média'] = media
    if sit == True:
        if media >= 6:
            dicionario['situação'] = 'Boa'
        elif media < 6:
            dicionario['situação'] = 'Ruim'
    print(dicionario)
    return dicionario

notas(9,10,3,6,7,8,1,2, sit=True)

