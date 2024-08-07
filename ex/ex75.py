valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))

print(f'Você digitou os valores {valores}')

print(f'O valor 9 aparececeu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O primeiro valor 3 aparececeu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram:', end=' ')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
