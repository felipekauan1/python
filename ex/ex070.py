print('Loja barata do Têra')
total = maisde1000 = maisbarato = c = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: R$ '))
    c += 1
    if c == 1 or preco < maisbarato:  # Adiciona o primeiro produto como o mais barato ou testa qual produto é o mais barato
        maisbarato = preco
        nomemaisbarato = nome
    total += preco
    if preco > 1000.0:  # testa quantos produtos custam mais de R$ 1000.00
        maisde1000 += 1
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    if continuar != 'S':
        break
print('Fim das compras!')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R$ {maisbarato:.2f}')
