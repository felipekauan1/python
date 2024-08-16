valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = valores[0]
        menor = valores[0]
    elif valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for e, v in enumerate(valores):
    if v == maior:
        print(f'{e}... ', end='')

print()

print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for e, v in enumerate(valores):
    if v == menor:
        print(f'{e}... ', end='')
