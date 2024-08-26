from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for item in lista:
        print(item, end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()

sorteia(numeros)
somaPar(numeros)
