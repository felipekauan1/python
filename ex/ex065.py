continuar = 'S'
somav = quanv = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    quanv += 1
    somav += n
    if quanv == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
media = somav / quanv
print(f'A média entre os {quanv} valores é de {media}')
print(f'O maior número digitado foi o {maior} e o menor foi o {menor}')
