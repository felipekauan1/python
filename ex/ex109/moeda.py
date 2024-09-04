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
