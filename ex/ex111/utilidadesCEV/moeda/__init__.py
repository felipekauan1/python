def resumo(preço, taxa_aumento, taxa_redução):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_aumento}% de aumento: \t{
          aumentar(preço, taxa_aumento, True)}')
    print(f'{taxa_redução}% de redução: \t{
          diminuir(preço, taxa_redução, True)}')
    print('-' * 35)


def moeda(r=0):
    rstr = f'R$ {r:.2f}'
    return rstr.replace('.', ',')


def aumentar(v, taxa, param=False):
    r = v + (v * taxa / 100)
    if param == True:
        return moeda(r)
    elif param == False:
        return r


def diminuir(v, taxa, param=False):
    r = v - (v * taxa / 100)
    if param == True:
        return moeda(r)
    elif param == False:
        return r


def dobro(v, param=False):
    r = v * 2
    if param == True:
        return moeda(r)
    elif param == False:
        return r


def metade(v, param=False):
    r = v / 2
    if param == True:
        return moeda(r)
    elif param == False:
        return r
