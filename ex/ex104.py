def leiaInt(dado):
    while True:
        valor = input(dado)

        if valor.isnumeric():
            return valor
        else:
            print('ERRO! Digite um número inteiro válido.')


v = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {v}')
