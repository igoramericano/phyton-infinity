import pygame
import time

pygame.init()
pygame.mixer.music.load('eminem.mp3')
pygame.mixer.music.play()

# Espera enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
