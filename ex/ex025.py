nome = str(input('Digite seu nome completo: ')).strip().title().split()

print(f'Seu nome tem a palavra "Silva"? {'Silva' in nome}')
