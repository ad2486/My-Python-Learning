'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
perfil_jogador = {}
gols_ppt = {}
total_gols = []
perfil_jogador['nome'] = str(input('Digite o nome do jogador: '))
perfil_jogador['partidas'] = int(input('Digite a quantidade de partidas jogadas pelo jogador: '))
for c in range(perfil_jogador['partidas']):
    gol = int(input(f'Quantos gols ele fez na {c+1}ª partida: '))
    gols_ppt[f'partida_{c}'] = gol
    total_gols.append(gol)
perfil_jogador['gols_ppt'] = gols_ppt
perfil_jogador['total_gols'] = sum(total_gols)
print(f'{'-='*45}\nO jogador {perfil_jogador["nome"]} tem tais estatísticas:\n{'-='*45}\nTotal de Gols => {perfil_jogador['total_gols']}\nTotal de Partidas => {perfil_jogador["partidas"]}')
for c, partida in enumerate(total_gols):
    print(f'Na {c+1}ª partida fez => {partida} Gols!')
    



