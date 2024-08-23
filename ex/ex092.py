from random import randint
from datetime import date
from time import sleep

jogo = dict()

jogo['idade'] = date.today().year - int(input('Digite o seu ano de nascimento: '))

print(jogo)
