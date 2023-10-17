"""
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

from pygame import mixer
from time import sleep

#Procura e Execução da musica
mixer.init()
mixer.music.load('musica.mp3') #Local da musica
mixer.music.play()
sleep(120)
