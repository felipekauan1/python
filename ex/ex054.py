from datetime import date

maior = 0
menor = 0
dataatual = date.today().year

for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = dataatual - ano
    if idade >= 21:
        print(f'Você tem {idade} anos em {dataatual} já é MAIOR DE IDADE')
        maior += 1
    else:
        print(f'Você tem {idade} anos em {dataatual} e NÃO é MAIOR DE IDADE')
        menor += 1
print(f'Das 7 pessoas {maior} são maior de idade e {menor} são de menor!')
