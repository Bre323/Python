from random import choice

nlist = [1, 2, 3, 4, 5]
nrand = choice(nlist)

print('Estou pensando em um número.....')
n = int(input('Digite um número de 1 a 5 para adivinhar: '))
print('\nO número que voce adivinhou é {}\n'.format(n))
print('O número escolhido é {}'.format(nrand))

if n == nrand:
    print('VOCE VENCEU!!!!!')
else:
    print('YOU LOOSE')
