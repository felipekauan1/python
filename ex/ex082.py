lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).lower()
    if continuar == 'n':
        break

for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
