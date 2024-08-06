n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = 0
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
          ''')
    opcao = int(input('Digite uma opção para realizar a operação: '))

    if opcao != 5:
        if opcao == 1:
            print(f'A soma de {n1} + {n2} = {n1 + n2}')
        elif opcao == 2:
            print(f'A multiplicação de {n1} * {n2} = {n1 * n2}')
        elif opcao == 3:
            if n1 > n2:
                print(f'O número {n1} é maior que o número {n2}')
            elif n2 > n1:
                print(f'O número {n2} é maior que o número {n1}')
            else:
                print(f'O número {n1} é igual ao número {n2}')
        elif opcao == 4:
            n1 = int(input('Digite um novo valor: '))
            n2 = int(input('Digite outro novo valor: '))
        else:
            print('Digite um opção valida!')

print('Saindo do programa...')
