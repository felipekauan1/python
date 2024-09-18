from pacotes import funcoes

while True:
    opção = funcoes.menu()

    if opção == 1:
        # ver pessoas cadastradas
        funcoes.ler_arquivo('documento.txt')
    elif opção == 2:
        # cadastrar nova pessoa
        funcoes.cadastrar('documento.txt')
    elif opção == 3:
        print('\033[35mSaindo do programa...\033[m')
        break
    else:
        print('\033[31mDigite um número entre 1 - 3\033[m')
