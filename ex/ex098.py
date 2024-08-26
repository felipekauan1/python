def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('-=' * 20)
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim - 1} de {passo} em {passo}')
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim + 1} de {abs(passo)} em {abs(passo)}')

    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('FIM!')


contador(1, 11, 1)
contador(10, -1, -2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(
    input('Fim: ')), int(input('Passo: ')))
