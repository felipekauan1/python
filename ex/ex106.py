def escreva(txt):
    print('~' * int(len(txt) + 4))
    print(f'  {txt}')
    print('~' * int(len(txt) + 4))


def ajuda():
    while True:
        escreva('SISTEMA DE AJUDA PyHELP')

        acessar = input('Função ou Biblioteca > ').lower()

        if acessar == 'fim':
            escreva('ATÉ LOGO!')
            break
        else:
            escreva(f"Acessando o manual do comando '{acessar}'")
            help(acessar)


ajuda()
