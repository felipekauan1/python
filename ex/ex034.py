salario = float(input('Digite o valor do seu salário: R$'))

if (salario > 1250):
    novo_salario = salario + (salario * 10 / 100)  # salario * 1.10
    print(f'Seu salário era R${salario} e agora recebeu um aumento de 10% e passa a valer R${novo_salario:.2f}')
else:
    novo_salario = salario * 1.15  # salario + (salario * 15 / 100)
    print(f'Seu salário era R${salario} e agora recebeu um aumento de 15% e passa a valer R${novo_salario:.2f}')
