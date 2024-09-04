def resumo(preço, taxa_aumento, taxa_redução):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'80% de aumento: {aumentar(preço, taxa_aumento, True)}')
    print(f'35% de redução: {diminuir(preço, taxa_redução, True)}')
    print('-' * 30)


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
