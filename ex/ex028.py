from random import randint
import pygame
from time import sleep

print('')
print('Jogo da Adivinhação')
print('-' * 21)

n = randint(1, 5)

num = int(input(
    'Tente descobrir qual foi o número entre 1 e 5 sorteado pelo computador: '))

print('Sorteando um número...')

sleep(1)

pygame.init()  # Inicia o pygame

if (num == n):
    print('Você acertoou! Venceu o desafio!')
    pygame.mixer.music.load('ex028-1.mp3')  # Carrega a música
    pygame.mixer.music.play()  # Toca a música
    input()  # Deve-se colocar um input() para tocar a música
else:
    print('Você errou! Tente outra vez!')
    pygame.mixer.music.load('ex028-2.mp3')  # Carrega a música
    pygame.mixer.music.play()  # Toca a música
    input()  # Deve-se colocar um input() para tocar a música

pygame.event.wait()  # Espera o programa terminar
