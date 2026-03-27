import pygame
pygame.init()
pygame.mixer.init()
musica = input("Do you want to listen Destá from Dorgival dantas? ").lower()
if musica == 'yes' or  musica == 'sim':
    audio = pygame.mixer.music.load('forrotoquemais-desta-3989c2.mp3')
    play = pygame.mixer.music.play()
stop = input('Do you want to stop the music? ').lower()
if stop == 'yes' or 'sim':
    paro = pygame.mixer.music.stop(play)