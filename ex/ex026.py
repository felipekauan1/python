nome = 'Ana Luiza Miranda Guimarães'.upper().strip()

print(f'Quantas vezes aparece a letra "A": {nome.count('A')}')

print(f'Em que posição ela aparece a primeira vez: {nome.find('A') + 1}')

print(f'Em que posição ela aparece a última vez: {nome.rfind('A') + 1}')
