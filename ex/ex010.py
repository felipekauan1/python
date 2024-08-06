reais = float(input('Quanto dinheiro você tem na carteira em reais? '))

dolares = reais / 3.27  # Considerei o dolar a R$ 3,17 como o Guanabara propôs

print(f'Com R$ {reais} você pode comprar {dolares:.2f} doláres.')
