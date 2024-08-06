vel = float(input('Digite a velocidade de um carro: '))

if (vel > 80):
    valor_multa = (vel - 80) * 7
    print(f'Você foi multado em R${valor_multa:.2f}!')
else:
    print('Você está dentro do limite de velocidade!')
