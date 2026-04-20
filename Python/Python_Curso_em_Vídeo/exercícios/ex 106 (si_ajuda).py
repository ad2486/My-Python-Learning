'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''

def sia():
    
    
    fundo_verde = '\033[1;30;42m'
    reset = '\033[m'
    fundo_azul = '\033[0;30;44m'
    fundo_branco = '\033[0;30;47m'
    linha = '~'*180
    
    while True:
        print(f'{fundo_verde}{linha}{reset}')
        print(f'{fundo_verde}{"SISTEMA DE AJUDA PYHELP":^180}{reset}')
        print(f'{fundo_verde}{linha}{reset}')
        ajuda = str(input('Função ou Biblioteca > ')).strip()
        texto = f'Acessando o manual do comando {ajuda}'
        if ajuda.upper() == 'FIM':
            break
        print(f'{fundo_azul}{linha}{reset}')
        print(f'{fundo_azul}{texto:^180}{reset}')
        print(f'{fundo_azul}{linha}{reset}')
        
        help(eval(ajuda))
       
        
    

sia()