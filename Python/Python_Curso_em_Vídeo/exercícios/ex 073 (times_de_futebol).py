'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''
brasileiro = ('Grêmio', 'Flamengo', 'Santos', 'Chapecoense', 'Avaí', 'Criciúma', 'Vitória', 'Vasco', 'Fluminense', 'Sport', 'Paysandu', 'São Paulo', 'Palmeiras', 'Bahia', 'Corinthians', 'Mirassol', 'Cruzeiro', 'Curitiba', 'Atlético Mineiro', 'Bragantino')

print(f'Os 5 primeiros times são: {brasileiro[:5]}')
print(f'Os lanternas são {brasileiro[-4:]}')
print(sorted(brasileiro))
print(f'A Chapecoense está na posição {brasileiro.index("Chapecoense") + 1}')