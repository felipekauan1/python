from datetime import date

anonascimento = int(input('Digite o ano de nascimento de um jovem: '))
anoatual = date.today().year

idade = anoatual - anonascimento

print(f'Você tem {idade} anos de idade em {anoatual}')
if idade < 18:
    print(f'Faltam {18 - idade} para você completar 18 anos')
    print('Você ainda vai se alistar no serviço militar')
    print(f'Seu alistamento será em {anonascimento + 18}')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print(f'Você passou {idade - 18} anos da idade obrigatória para alistamento')
    print('Já passou do tempo do alistamento')
    print(f'Seu alistamento deveria ter sido em {anonascimento + 18}')
