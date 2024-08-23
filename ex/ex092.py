# importações
from random import randint
from datetime import date
from time import sleep

# criando o dicionário dados
dados = dict()

# lendo o nome
dados['nome'] = str(input('Nome: '))

# lendo o ano de nascimento
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
# calculando a idade (data atual menos o ano de nascimento)
dados['idade'] = date.today().year - ano_nascimento

# lendo a carteira de trabalho(CTPS)
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# se tiver carteira de trabalho irá ler itens adicionais
if dados['CTPS'] != 0:
    # lendo o ano de contratação
    dados['ano de contratação'] = int(input('Ano de Contratação: '))

    # lendo o salário
    dados['salário'] = float(input('Salário: R$ '))

    # calculando a idade que irá se aposentar
    dados['aposentadoria'] = dados['ano de contratação'] - ano_nascimento + 35

print('=-=' * 10)

for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')
