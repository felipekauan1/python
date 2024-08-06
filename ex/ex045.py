from random import randint
from time import sleep

jogador = int(input('''Pedra, Papel, Tesoura? 
[0] PEDRA                     
[1] PAPEL                     
[2] TESOURA                     

Qual é a sua jogada? '''))

computador = randint(0, 2)

lista = ['PEDRA', 'PAPEL', 'TESOURA']

print('')
sleep(.8)
print('JO')
sleep(.8)
print('KEN')
sleep(.8)
print('PÔ')
print('')

print(f'JOGADOR jogou {lista[jogador]}')
print(f'COMPUTADOR jogou {lista[computador]}')

if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADOR VENCEU!')
elif jogador == 1:
    if computador == 0:
        print('JOGADOR VENCEU!')
    elif computador == 1:
        print('EMPATE!')
    else:
        print('COMPUTADOR VENCEU!')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR VENCEU!')
    elif computador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('EMPATE!')
else:
    print('Digite uma opção valida para jogar!')
