def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = str(input('Nome do jogador: '))
g= int(input('Número de gols: '))

print(ficha(nome=n, gols=g))
