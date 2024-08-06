from math import pow, sqrt, hypot

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# hipotenusa = (oposto**2 + adjacente**2)**(.5)
# hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2))
hipotenusa = hypot(oposto, adjacente)

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
