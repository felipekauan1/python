nota1 = float(input('Digite sua PRIMEIRA nota: '))
nota2 = float(input('Digite sua SEGUNDA nota: '))

media = (nota1 + nota2) / 2

print(f'Sua nota média foi de {media:.1f}')

if media < 5:
    print('REPROVADO!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')