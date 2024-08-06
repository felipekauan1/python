tupla = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESEIS', 'DEZESETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n = int(input('Digite um número entre 0 e 20. Maior que 20 para o programa: '))
    if 0 <= n <= 20: 
        print(tupla[n])
    else:
        break
print('Programa encerrado.')
