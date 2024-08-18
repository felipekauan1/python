pessoas = []
dados = []
totpessoas = 0
maispesados = []
maisleves = []

# recebe o nome e peso das pessoas e adiciona-os a lista
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    # adiciona a cópia a lista dados na lista pessoas
    pessoas.append(dados.copy())
    totpessoas += 1  # conta quantas pessoas foram cadastradas
    dados.clear()  # limpa a lista dados antes de ler novos dados

    # verifica se o usuário quer ou não continuar cadastrando novos dados
    continuar = str(input('Quer continuar? [S/N] ')).capitalize()
    if continuar == 'N':
        break

# identifica qual foi o maior e o menor peso da lista
for e, p in enumerate(pessoas):
    if e == 0:
        maiorpeso = p[1]
        menorpeso = p[1]
    if p[1] > maiorpeso:
        maiorpeso = p[1]
    if p[1] < menorpeso:
        menorpeso = p[1]

# identifica o nome dos mais leves e mais pesados
for p in pessoas:
    if p[1] == maiorpeso:
        # maispesadaos recebe o nome das pessoas mais pesadas
        maispesados.append(p[0])
    if p[1] == menorpeso:
        # maisleves recebe o nome das pessoas mais leves
        maisleves.append(p[0])

print(f'Ao todo foram cadastradas {totpessoas} pessoas na lista')

print(f'O maior peso foi de {maiorpeso} Kg. Peso de {maispesados}')

print(f'O menor peso foi de {menorpeso} Kg. Peso de {maisleves}')
