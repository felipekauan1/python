def moeda(r=0):
    rstr = f'R$ {r:.2f}'
    return rstr.replace('.', ',')


def aumentar(v, a):
    r = v + (v * a / 100)
    return r


def diminuir(v, d):
    r = v - (v * d / 100)
    return r


def dobro(v):
    r = v * 2
    return r


def metade(v):
    r = v / 2
    return r
