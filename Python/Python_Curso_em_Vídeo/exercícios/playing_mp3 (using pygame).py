import pygame
import os
import random
pygame.init()
pasta = r'C:\Users\arthu\OneDrive\Área de Trabalho\yt\terraria infernum\audio'
musicas = [arquivo for arquivo in os.listdir(r'C:\Users\arthu\OneDrive\Área de Trabalho\yt\terraria infernum\audio') if arquivo.endswith('.mp3')]
if musicas:
    musica = random.choice(musicas)
    caminho = os.path.join(pasta, musica)
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()
    print (f'Tocando: {musica}')
    input ('Pressione Enter para parar')
else:
    print ('Não há arquivos .mp3')
