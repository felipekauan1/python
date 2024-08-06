# nome = str(input('Digite seu nome completo: '))
nome = 'Ana Luiza Miranda Guimarães'

print(f'O nome com todas as letras maiúsculas: {nome.upper()}')
print(f'O nome com todas as letras minúsculas: {nome.lower()}')

lista_nome = nome.split()

print(f'Quantas letras ao todo sem considerar os espaços: {
      len(''.join(lista_nome))}')

primeiro_nome = len(lista_nome[0])

print(f'Quantas letras tem o primeiro nome: {primeiro_nome}')
