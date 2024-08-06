distancia = float(input('Qual é a distancia da viagem em Km? '))

if (distancia <= 200):
    preco_passagem = distancia * 0.5
    print(f'O preço da passagem cobrando R$0,50 por Km rodado é R${
          preco_passagem:.2f}')
else:
    preco_passagem = distancia * 0.45
    print(f'O preço da passagem cobrando R$0,45 por Km rodado é R${
          preco_passagem:.2f}')
