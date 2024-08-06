preco = float(input('Digite o preço do produto: R$ '))
pagamento = int(input('''Qual é a condição de pagamento? 
[1] À vista dinheiro/cheque                     
[2] À vista no cartão                     
[3] 2x no cartão                     
[4] 3x ou mais no cartão

-> '''))

if pagamento == 1:
    print('Pagamento à vista dinheiro/cheque: 10% de desconto')
    precofinal = preco * .9
    print(f'O preço final do produto foi de R$ {precofinal:.2f}')
elif pagamento == 2:
    print('Pagamento à vista no cartão: 5% de desconto')
    precofinal = preco * .95
    print(f'O preço final do produto foi de R$ {precofinal:.2f}')
elif pagamento == 3:
    print('Pagamento em até 2x no cartão: Preço normal')
    print(f'Sua compra será parcelada em 2x de R$ {preco / 2:.2f} SEM JUROS')
    print(f'O preço final do produto foi de R$ {preco:.2f}')
elif pagamento == 4:
    print('Pagamento 3x ou mais no cartão: 20% de juros')
    precofinal = preco * 1.2
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${precofinal / parcelas:.2f} COM JUROS')
    print(f'O preço final do produto foi de R$ {precofinal:.2f}')
else:
    print('Digite uma opção valida!')
