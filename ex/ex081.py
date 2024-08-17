lista = []
quantidade_numeros = 0

while True:
    n = int(input('Digite um número: '))
    quantidade_numeros += 1
    lista.append(n)

    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar != 'S':
        break

print(f'Você digitou {quantidade_numeros} números')

if 5 in lista:
    print(f'O valor 5 faz parte da lista, e está na posição ', end='')
    for e, item in enumerate(lista):
        if item == 5:
            print(f'{e}... ', end='')
    print()
else:
    print('O valor 5 não faz parte da lista')

lista.sort(reverse=True)
print(f'Os valores na ordem decrescente são {lista}')
