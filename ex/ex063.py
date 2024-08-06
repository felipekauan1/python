print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))

primeiro = 0
segundo = 1
c = 3

print(f'{primeiro} -> {segundo} -> ', end='')


while c <= n:
    proximo = primeiro + segundo
    print(proximo, end=' -> ')
    c += 1
    primeiro = segundo
    segundo = proximo

print('Fim')
