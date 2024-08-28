def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número
    """
    if show == True:  # se show for igual True faça:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(f'{c} x ', end='')
        print(f'= {f}')
    elif show == False:  # senão, se show for igual a False faça:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        print(f)


fatorial(5, True)
