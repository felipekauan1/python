def linha():
    print('-' * 30)


def escreva(msg):
    linha()
    print(f'\033[32m\033[1m{msg}\033[m'.center(41))
    linha()


def cabeçalho():
    escreva('MENU PRINCIPAL')
    print('\033[34m\033[1m1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema\033[m')
    linha()


def menu():
    import os
    from time import sleep

    while True:
        cabeçalho()
        try:
            opção = int(input('\033[33m\033[1mSua opção: \033[m'))
        except (TypeError, ValueError):
            print('\033[31mDigite um número inteiro valido!\033[m')
        except KeyboardInterrupt:
            print('\033[4mPrograma interrompido pelo usuário!\033[m')
        else:
            break

        sleep(.7)
        os.system('cls')

    sleep(.7)
    os.system('cls')
    return opção


def ler_arquivo(nome_documento):
    try:
        with open(nome_documento, 'rt') as documento:
            conteudo = documento.read()
    except FileNotFoundError:
        print('\033[36mAinda não existe nenhuma pessoa cadastrada!\033[m')
    else:
        escreva('PESSOAS CADASTRADAS')
        print(conteudo)




def cadastrar(nome_documento):
    """
    -> Cadastra pessoas e cria um arquivo.txt se não houver um
    """

    escreva('NOVO CADASTRO')
    with open(nome_documento, 'a') as documento:
        nome = input('Nome: ')
        idade = input('Idade: ')
        documento.write(f'{nome:<25}{idade:>3}\n')
    print(f'\033[34m\033[1mNovo registro de {nome} adicionado.\033[m')
