saque = int(input('Digite o valor a ser sacado: R$ '))
cedula = 50
totCedula = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if saque == 0:
            break
