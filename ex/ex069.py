mais18 = homens = menos20 = 0
while True:
    print('CADASTRAR PESSOAS')
    idade = int(input('Idade: '))
    while True:  # Valida se o sexo está correto
        sexo = str(input('Sexo: ')).strip().upper()
        if sexo in 'FM':
            break
    if idade > 18:  # Testa quantas pessoas tem mais de 18 anos
        mais18 += 1
    if sexo == 'M':  # Testa quantos homens foram cadastrados
        homens += 1
    if sexo == 'F' and idade < 20:  # Testa quantas mulheres menores de 20 anos foram cadastrados
        menos20 += 1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar != 'S':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {menos20} mulheres com menos de 20 anos')
