lista = []

for i in range(0, 5):
    valor = int(input(f'Digite o valor para a posição {i}: '))
    if valor not in lista: 
        lista.append(valor)
        print('Adicionado ao final da lista...')
        