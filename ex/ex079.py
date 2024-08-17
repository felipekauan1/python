valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar != 'S':
        break

valores.sort()

print(f'Você digitou os valores {valores}')
