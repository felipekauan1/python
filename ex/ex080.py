lista = []

for i in range(0, 5):
    valor = int(input(f'Digite o valor para a posição {i}: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado no final da lista')
    else:
        for c in range(0, len(lista)):
            if valor < lista[c]:
                lista.insert(c, valor)
                print(f'O valor {valor} foi adicionado na posição {c} da lista')
                break

print(f'Os valores digitados na ordem foram {lista}')
