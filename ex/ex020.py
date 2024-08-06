'''
from random import sample

lista = ['Felipe', 'Guanabara', 'Ana', 'Maria']

ordem = sample(lista, len(lista))

print(f'O ordem sorteada dos alunos é: {ordem}')
'''

from random import shuffle

lista = ['Felipe', 'Guanabara', 'Ana', 'Maria']

shuffle(lista)

print(f'O ordem sorteada dos alunos é: {lista}')
