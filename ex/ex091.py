from random import randint

jogo = dict()

for i in range(1, 5):
    jogo[f'Jogador {i}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

lista_jogo = list(jogo.values())

print(f'O vencedor foi o jogador que tirou {max(lista_jogo)}')
