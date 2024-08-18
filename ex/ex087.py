matriz = [[], [], []]
soma_pares = soma_3_coluna = 0

# ler os valores da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

# mostra a matriz na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()

# calcula a soma dos números pares da matriz
for linha in matriz:
    for coluna in linha:
        if coluna % 2 == 0:
            soma_pares += coluna

# calcula a soma dos números da 3º coluna da matriz
for linha in matriz:
    soma_3_coluna += linha[2]

# calcula o maior valor da segunda linha da matriz
for e, c in enumerate(matriz[1]):
    if e == 0 or c > maior:
        maior = c

# mostra o resultado dos calculos realizados
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_3_coluna}')
print(f'O maior valor da segunda linha é {maior}')
