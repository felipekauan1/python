lista1 = str(input('Digite uma frase para verificar se ela é um PALINDROMO: ')).split()
frase = ''.join(lista1)
frasecontrario = ''

for c in range(len(frase) - 1, -1 , -1):
    frasecontrario += frase[c]

if frase == frasecontrario:
    print(f'A frase {frase} ao contrario é {
          frasecontrario} e ela é um PALINDROMO!')
else:
    print(f'A frase {frase} ao contrario é {
          frasecontrario} e ela NÃO é um PALINDROMO!')
