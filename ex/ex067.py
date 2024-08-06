while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1
print('Programa encerrado')
