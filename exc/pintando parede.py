l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

area = l*a
ltinta = area/2

print('-'*50)
print('A parede possui uma área de {:.2f}' .format(area))
print('Tinta necessária: {:.2f} litros' .format(ltinta))
print('-'*50)
