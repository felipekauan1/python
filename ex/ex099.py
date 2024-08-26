from time import sleep


def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for e, v in enumerate(valores):
        if e == 0 or v > maior:
            maior = v

        print(v, end=' ', flush=True)
        sleep(.3)

    print(f'Forma informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi o {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
