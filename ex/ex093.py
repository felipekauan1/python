jogador = {}
aproveitamento = []

jogador['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador['nome']} jogou: '))

for c in range(0, partidas):
    aproveitamento.append(int(input(f'Quantidade de gols na {c}º partida: ')))

jogador['gols'] = aproveitamento.copy()

jogador['total de gols'] = sum(aproveitamento)

print('=-=' * 20)

print(jogador)

print('=-=' * 20)

for k, v in jogador.items():
    print(f'O Campo {k} tem o valor {v}.')

print('=-=' * 20)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for e, a in enumerate(aproveitamento):
    print(f'Na partida {e}, fez {a} gols.')

print(f'Foi um total de {jogador["total de gols"]} gols.')
