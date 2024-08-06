n = int(input('Digite um número inteiro: '))
base = int(input('''Digite qual será a base de conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL
                 
-> '''))


if base == 1:
    print(f'O valor {n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
else:
    if base == 2:
        print(f'O valor {n} convertido para OCTAL é igual a {oct(n)[2:]}')
    else:
        if base == 3:
            print(f'O valor {n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
        else:
            print('Digite uma opção valida!')
