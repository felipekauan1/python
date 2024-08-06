s = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s +=  c
print(f'A soma de todos os números impares que são multiplos de 3 no intervalo de 1 a 500 é: {s}')
