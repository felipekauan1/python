from math import radians, sin, cos, tan  # importei o modulo

graus = float(input('Digite o valor do ângulo: '))  # Ler o ângulo em graus

radiano = radians(graus)  # Transforma o valor do ângulo de graus para radianos

seno = sin(radiano)  # Pega o seno do radiano
cosseno = cos(radiano)  # Pega o cosseno do radiano
tangente = tan(radiano)  # Pega a tangente do radiano

# Printa o seno, cosseno e tangente
print(f'Valor do seno {seno:.2f}')
print(f'Valor do cosseno {cosseno:.2f}')
print(f'Valor da tangente {tangente:.2f}')
