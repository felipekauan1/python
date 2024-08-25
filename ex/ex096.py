def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura:.1f} x {comprimento:.1f} é de {area_terreno:.1f}m²')


print('CONTROLE DE TERRENOS')
print('-' * 30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

print('-' * 30)
area(largura, comprimento)