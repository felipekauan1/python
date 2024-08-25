rapaziada = []
pessoa = {}
soma_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        else:
            print('Digite um sexo valido!')

    pessoa['idade'] = int(input('Idade: '))

    # adiciona os dados da pessoa na lista
    rapaziada.append(pessoa.copy())
    # limpa os dados da pessoa
    pessoa.clear()

    # se a resposta for sim, irá reiniciar a estrutura de repetição
    resposta = str(input('Quer continuar? [S/N] '))[0]
    if resposta in 'Nn':
        break

print(f'O grupo tem {len(rapaziada)} pessoas.')

for p in rapaziada:
    soma_idade += p['idade']

media = soma_idade / len(rapaziada)

print(f'A média de idade é de {media:.2f} anos.')

print(f'As mulheres cadastradas foram: ', end='')
for p in rapaziada:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()

print(f'Lista das pessoas que estão acima da média de idade: ')
print()

for p in rapaziada:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
        print()

print('Programa encerrado!')
