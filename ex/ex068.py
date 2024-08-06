from random import randint
vitorias = 0
while True:
    escolhajogador = str(input('Par ou Impar [P/I]: ')).strip().upper()
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        if escolhajogador == 'P':
            print(f'Você jogou {jogador} e o computador {
                  computador}. Total de {soma}, deu PAR')
            print('Você venceu!')
            print('Vamos jogar novamente...')
            vitorias += 1
        elif escolhajogador == 'I':
            print(f'Você jogou {jogador} e o computador {
                  computador}. Total de {soma}, deu PAR')
            print('Você perdeu!')
            print('GAME OVER!')
            break
        else:
            print('Digite um valor valido!')
    else:
        if escolhajogador == 'I':
            print(f'Você jogou {jogador} e o computador {
                  computador}. Total de {soma}, deu IMPAR')
            print('Você venceu!')
            print('Vamos jogar novamente...')
            vitorias += 1
        elif escolhajogador == 'P':
            print(f'Você jogou {jogador} e o computador {
                  computador}. Total de {soma}, deu IMPAR')
            print('Você perdeu!')
            print('GAME OVER!')
            break
        else:
            print('Digite um valor valido!')
print(f'Você venceu {vitorias} vezes.')
