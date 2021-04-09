print('='*20)
print('Progressão Aritmética')
print('='*20)
pri = int(input('\nPrimeiro número: '))
raz = int(input('Razão: '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec+raz, raz):
    print('{}'.format(c), end=' ')
