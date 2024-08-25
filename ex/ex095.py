time = []
jogador = {}
aproveitamento = []

while True:
    # lendo o nome do jogador
    jogador['nome'] = str(input('Nome do jogador: '))

    # lendo quantas partidas ele jogou
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou: '))

    # lendo a quantidade de gols marcados por partida e adicionando na lista aproveitamento
    for c in range(0, partidas):
        aproveitamento.append(
            int(input(f'Quantidade de gols na {c}º partida: ')))

    # copia a lista de aproveitamento
    jogador['gols'] = aproveitamento.copy()

    # calcula o total de gols na lista de aproveitamento do jogador
    jogador['total de gols'] = sum(aproveitamento)

    # limpa a lista de aproveitamento
    aproveitamento.clear()

    # adiciona o dicionário jogador a lista time
    time.append(jogador.copy())

    # limpa o dicionário jogador
    jogador.clear()

    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        else:
            print('Erro. Digite apenas S ou N.')
    if resposta == 'N':
        break

# mostra as keys do discionário
print('=-=' * 20)
print('ID   ', end='')
for k in time[0].keys():
    print(f'{k:<10}', end='')
print()

# mostra o id e os valores de cada discionário na lista time
print('---' * 20)
for e, jogador in enumerate(time):
    print(f'{e:4>}   ', end='')
    for valor in jogador.values():
        print(f'{str(valor):<10}', end='')
    print()
print('=-=' * 20)

while True:
    id = int(input('Mostrar dados de qual jogador? (999 para parar): '))

    if id == 999:
        print('Encerrando programa...')
        break

    # valida se foi digitado um id correto
    if id < 0 or id >= len(time):
        print(f'Digite um valor valido! Não existe o ID {id}')
    else:
        # se for um id correto
        print(f'Levantamento do jogador {time[id]['nome']}:')

        for e, g in enumerate(time[id]['gols']):
            print(f'No jogo {e + 1} fez {g} gols')
