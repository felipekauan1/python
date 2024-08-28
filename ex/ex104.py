def leiaInt(v):
    while True:
        inputv = input(v)
        print(type(inputv))
        if 'int' in str(type(inputv)):
            break
        else:
            print('ERRO! Digite um número inteiro válido.')

    return inputv


valor = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {valor}')
