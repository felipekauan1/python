alunos = []
dados_aluno = []

while True:
    dados_aluno.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados_aluno.append(media)
    alunos.append(dados_aluno.copy())
    dados_aluno.clear()

    continuar = str(input('Quer continuar? [S/N]')).capitalize()
    if continuar == 'N':
        break

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 1:
        print(f'{alunos[0]}')

    if mostrar == 999:
        break
