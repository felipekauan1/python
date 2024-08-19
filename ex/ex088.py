from random import randint
from time import sleep

jogos = []

quantos_jogos = int(input('Quantos jogos você quer que eu sorteie: '))

# faz o sorteio e printa os números sorteados
for l in range(0, quantos_jogos):
    jogos.append([])  # adiciona uma lista vazia no final da lista jogos

    for c in range(0, 6):  # adiciona 6 valores aleatórios na lista jogos
        while True:
            aleatorio = randint(1, 60)
            if aleatorio not in jogos[l]:  # se o número sorteado não estiver na lista jogos[l], o número é adicionado a lista e o laço é encerrado
                jogos[l].append(aleatorio)
                break

    jogos[l].sort()

    print(f'Jogo {l + 1}: {jogos[l]}')  # printa a lista na posição [l]

    sleep(.7)  # espera 0.7s
