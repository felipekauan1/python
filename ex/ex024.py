nome_cidade = str(input('Digite o nome da cidade: ')).strip().title().split()

print(f'O nome da cidade começa com "Santo"? {nome_cidade[0] == 'Santo'}')
