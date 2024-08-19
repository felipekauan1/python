from random import randint
from time import sleep

jogos = []

quantos_jogos = int(input('Quantos jogos você quer que eu sorteie: '))

# faz o sorteio e printa os números sorteados
for l in range(0, quantos_jogos):
    jogos.append([])  # adiciona uma lista vazia no final da lista jogos

    for c in range(0, 6):  # adiciona 6 valores aleatórios na lista jogos
        # testa se o valor aleatório não está na lista jogos[l]
        while True:
            aleatorio = randint(0, 4)
            # se o valor aleatório estiver na lista ele será sorteado outra vez
            if aleatorio in jogos[l]:
                continue
            # senão estiver na lista o valor aleatório é adicionado na lista jogos[l] e o laço e encerrado
            else:
                jogos[l].append(aleatorio)
                break

    jogos[l].sort()

    print(f'Jogo {l + 1}: {jogos[l]}')  # printa a lista na posição [l]

    sleep(.7)  # espera 0.7s
