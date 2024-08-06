somaidade = 0
maioridade = 0
menosde20 = 0

for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [F/M]: ')).upper()
    somaidade += idade  # somando as idades do grupo
    if sexo == 'M' and idade > maioridade:  # testando qual é a maior idade
        maioridade = idade
        maisvelho = nome  # pegando o nome do homem mais velho
    if sexo == 'F' and idade < 20:  # testando quantas mulheres tem menos de 20 anos
        menosde20 += 1

mediaidade = somaidade / 4  # calculando a média de idade do grupo

print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho é o {maisvelho} com {maioridade} anos de idade')
print(f'{menosde20} mulheres tem menos de 20 anos')
