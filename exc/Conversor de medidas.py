dist = float(input('Digite a sua distancia em metros: '))

mm = dist*1000
cm = dist*100
dm = dist*10
dam = dist/10
hm = dist/100
km = dist/1000

print('='*50)
print('medida em milimetros: {}' .format(mm))
print('medida em centimetros: {}' .format(cm))
print('medida em decimetros: {}' .format(dm))
print('medida em metros: {}' .format(dist))
print('medida em decametros: {}' .format(dam))
print('medida em hectometros: {}' .format(hm))
print('medida em kilometros: {}' .format(km))
