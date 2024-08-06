from datetime import date

ano = int(input('Digite um ano qualquer: '))

if (ano == 0):
    ano = date.today().year

print(ano)

if (ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
