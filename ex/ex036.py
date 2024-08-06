valorcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: '))
anos = float(input('Digite em quantos anos você irá pagar: '))

meses = anos * 12  # Transforma a quantidades de anos para mêses

prestacao = valorcasa / meses

print(f'Para pagar uma casa de R$ {valorcasa:.2f}, o valor da prestação mensal é de R${prestacao:.2f}')

if prestacao <= salario * 0.3:
    print('Emprestimo aceito!')
else:
    print('Emprestimo negado!')
