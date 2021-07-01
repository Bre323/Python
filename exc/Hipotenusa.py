from math import hypot

n = int(input('Digite o valor dos primeiro cateto: '))
n2 = int(input('Digite o valor do segundo cateto: '))
hip = hypot(n, n2)

print('Primeiro cateto: ', n)
print('Segundo cateto: ', n2, '\n\n')
print('='*50)
print('Hipotenusa >>> ', hip)
print('='*50)
