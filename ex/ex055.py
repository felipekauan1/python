for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))  
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso

print(f'O maior peso digitado foi: {maiorpeso}')
print(f'O menor peso digitado foi: {menorpeso}')
