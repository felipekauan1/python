valores = []
pmaior = []
pmenor = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

print(f'Você digitou os valores {valores}')

for e, v in enumerate(valores):
    if e == 0:
        maior = v
        menor = v
    if v >= maior:
        maior = v
        pmaior.append(valores.index(v))
    if v <= menor:
        menor = v
        pmenor.append(valores.index(v))

print(f'O maior valor digitado foi {maior} nas posições {pmaior}')
print(f'O menor valor digitado foi {menor} nas posições {pmenor}')
