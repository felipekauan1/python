from random import randint
from time import sleep

print('')
print('Jogo da Adivinhação')
print('-' * 21)

print('Sorteando um número entre 0 e 10...')
sleep(.5)

computador = randint(0, 10)
jogador = 11
palpites = 0

while jogador != computador:
    jogador = int(input(
        'Tente descobrir qual foi o número entre 0 e 10 sorteado pelo computador: '))

    palpites += 1

    if (jogador == computador):
        print('Você acertoou! Venceu o desafio!')
    else:
        if (jogador < computador):
            print('Mais... Tente outra vez!')
        else:
            print('Menos... Tente outra vez!')


print(f'Você tentou {palpites} palpites para acertar')
