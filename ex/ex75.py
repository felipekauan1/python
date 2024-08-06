v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite outro valor: '))
v4 = int(input('Digite outro valor: '))

valores = (v1, v2, v3, v4)

print(f'Você digitou os valores {valores}')

print(f'O valor 9 aparececeu {valores.count(9)} vezes')

print(f'O primeiro valor 3 aparececeu na {valores.index(3) + 1}ª posição')

pares = ''
for c in valores:
    if c % 2 == 0:
        pares += f'{c} '

print(f'Os valores pares digitados foram: {pares}')
