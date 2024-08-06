import pygame

pygame.init()  # Inicia o pygame

pygame.mixer.music.load('ex021.mp3')  # Carrega a música

pygame.mixer.music.play()  # Toca a música

input()  # Deve-se colocar um input() para tocar a música

pygame.event.wait()  # Espera o programa terminar
