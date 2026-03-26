import vlc
import time
player = vlc.MediaPlayer(r"C:\Users\arthu\OneDrive\Área de Trabalho\yt\terraria infernum\audio\hellcat.mp3")
player.play()
time.sleep(2)
while player.is_playing():
    time.sleep(0.2)
