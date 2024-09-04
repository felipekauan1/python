import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, param=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, param=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, param=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, param=True)}')
