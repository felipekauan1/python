


def voto(anonasc):
    from datetime import date
    
    idade = date.today().year - anonasc

    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('Voto Negado.')
    elif 16 <= idade < 18 or idade >= 65:
        print('Voto Opcional.')
    else:
        print('Voto Obrigatório.')


voto(int(input('Em que ano você nasceu? ')))
