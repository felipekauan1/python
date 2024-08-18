lista = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Todos os itens da lista: {lista}')

lista[0].sort()
lista[1].sort()

print(f'Os valores pares da lista em ordem crescente são {lista[0]}')
print(f'Os valores impares da lista em ordem crescente são {lista[1]}')
