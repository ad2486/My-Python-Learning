'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

'''
jogadores = {}
while True:
    perfil_jogador = {}
    gols_ppt = {}
    total_gols = []
    nome = str(input('Digite o nome do jogador: '))
    perfil_jogador['nome'] = nome
    perfil_jogador['partidas'] = int(input('Digite a quantidade de partidas jogadas pelo jogador: '))
    for c in range(perfil_jogador['partidas']):
        gol = int(input(f'Quantos gols ele fez na {c+1}ª partida: '))
        gols_ppt[f'partida_{c}'] = gol
        total_gols.append(gol)
    perfil_jogador['gols_ppt'] = gols_ppt
    perfil_jogador['total_gols'] = sum(total_gols)
    jogadores[nome] = perfil_jogador
    op = str(input('Deseja continuar? (S/N)')).upper().strip()
    if op == 'S':
        continue
    elif op == 'N':
        break
    

for jogador in jogadores:
    print(f'Estatísticas: {jogadores[jogador]}')