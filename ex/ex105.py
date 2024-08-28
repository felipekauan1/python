def notas(* variasnotas, sit=False):
    """
    -> Função para analizar notas e situações de varios alunos.
    :param variasnotas: tupla com todas as notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não indicar a situação
    :return: Dicionário com varias informações sobre o aluno
    """

    aluno = dict()

    aluno['total'] = len(variasnotas)
    aluno['maior'] = max(variasnotas)
    aluno['menor'] = min(variasnotas)
    aluno['média'] = sum(variasnotas) / len(variasnotas)

    if sit == True:
        if aluno['média'] <= 3:
            aluno['situação'] = 'RUIM'
        elif 3 < aluno['média'] <= 7:
            aluno['situação'] = 'RAZOÁVEL'
        elif aluno['média'] > 7:
            aluno['situação'] = 'BOA'

    return aluno

print('=-' * 30)
print(notas(10, 9, 8, sit=True))
print('=-' * 30)
help(notas)
print('=-' * 30)
print(notas.__doc__)
