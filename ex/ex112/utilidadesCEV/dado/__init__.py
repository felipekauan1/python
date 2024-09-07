from utilidadesCEV import moeda


def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido.\033[0m')
        else:
            print(f'\033[33mBOA: "{entrada}" é um preço válido.\033[0m')
            return float(entrada)
