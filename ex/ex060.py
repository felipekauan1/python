n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f)

print(f'O fatorial de {n} é igual a {f}')

# Calculo do fatorial usando o for
"""n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
c = n

for c in range(c, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c

print(f)
"""