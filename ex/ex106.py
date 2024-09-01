def escreva(txt):
    print('~' * int(len(txt) + 4))
    print(f'  {txt}')
    print('~' * int(len(txt) + 4))


def ajuda():
    while True:
        print(cores[1], end='')
        escreva('SISTEMA DE AJUDA PyHELP')
        print(cores[0], end='')

        print(cores[2], end='')
        acessar = input('Função ou Biblioteca > ').lower()
        print(cores[0], end='')

        if acessar == 'fim':
            print(cores[3], end='')
            escreva('ATÉ LOGO!')
            break
        else:
            print(cores[5], end='')
            escreva(f"Acessando o manual do comando '{acessar}'")
            print(cores[0], end='')

            help(acessar)


cores = [f'\033[0m', f'\033[43m\033[1m', f'\033[34m\033[1m',
         f'\033[41m\033[1m', f'\033[45m\033[1m', f'\033[47m\033[1m']

ajuda()
