'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
largura = 40
print(largura*'-')
print(f'{'LISTAGEM DE PREÇOS':^40}')
print(largura*'-')
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30} R${listagem[pos+1]:>7.2f}')

#Tô usando o contador pos do loop for pra fazer a progressão das leituras na tupla, o 0 mostra que vai começar do início, creio que dá pra botar um :len(listagem) direto nesse caso
#O len(listagem) tá dizendo pra ir até o final da tupla não importando o tamanho
# O 2 tá fazendo pular de 2 em 2 


