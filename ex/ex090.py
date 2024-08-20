aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Digite a média de {aluno["Nome"]}: '))

# verifica se o aluno está aprovado ou reprovado
if aluno['Media'] > 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] <= 7:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
