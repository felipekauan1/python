a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da trerceira reta: '))

if (a < b + c and b < a + c and c < a + b):
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
