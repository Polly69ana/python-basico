# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Importar biblioteca
import pygame

# Inicia todos os módulos do Pygame
pygame.init()

# Ultilizada para carregar arquivo de áudio
pygame.mixer.music.load('peterpan.mp3')

# Coloca a música para tocar
pygame.mixer.music.play()


pygame.event.wait()
input()