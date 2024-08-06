n = int(input('Digite um número para descobrir se ele é primo: '))

tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print(f'[{n}]', end=' ')
    else:   
        print(n, end=' ')
print(f'O número {n} foi divísivel por {tot} números')
if tot == 2:
    print(f'O número {n} é PRIMO')
else:
    print(f'O número {n} NÃO é PRIMO')
