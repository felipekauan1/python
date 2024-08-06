n = quantos = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        quantos += 1
        soma += n

print(f'Foram digitados {quantos} números e a soma entre eles é {soma}')