from datetime import date

anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc

print(f'Você tem {idade} anos de idade em {anoatual} e sua categoria é:')

if (idade <= 9):
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')