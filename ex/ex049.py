valor = int(input('Digite um valor para ver sua taboada: '))

for c in range(10, -1, -1):
    print(f'{c} x {valor} = {c * valor}')

# for c in range(10, 0, -1):
#     for i in range(10, -1, -1):
#         print(f'{c} x {i} = {c * i}')
#     print('-=' * 11)
