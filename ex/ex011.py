largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
litros = area / 2

print(f'A área da parede é {area}m²')
print(f'A quantidade de tinta necessária para pintar a parede é de {
      litros} litros')
