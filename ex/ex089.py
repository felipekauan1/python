alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = str(input('Quer continuar? [S/N]')).capitalize()
    if continuar == 'N':
        break

print('=-' * 13)
print(f'{'ID':<7}{'nome':<10}{'Media':>8}')
print('-=' * 13)

for c in range(0, len(alunos)):
    print(f'{c:<7}{alunos[c][0]:<10}{alunos[c][2]:>8}')

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if len(alunos) > mostrar:
        print(f'As notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}')

    if mostrar == 999:
        break

print('Programa encerrado...')
