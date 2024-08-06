from random import randint

listagem = (randint(0, 100), randint(0, 100), randint(
    0, 100), randint(0, 100), randint(0, 100))

for i, c in enumerate(listagem):
    if i == 0:
        menor = c
        maior = c
    if c < menor:
        menor = c
    if c > maior:
        maior = c

print(listagem)
print(f'O menor valor sorteado foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')
