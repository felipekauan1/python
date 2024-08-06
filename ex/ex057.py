sexo = 'd'
while sexo not in 'FM':
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()
    if sexo not in 'FM':
        print('Erro, tente novamente. Digite um sexo valido!')
    else:
        print(f'Você digitou o sexo {sexo}, seu sexo foi validado com sucesso!')
