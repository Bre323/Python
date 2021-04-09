num = list()
par = list()
impar = list()

while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print('-'*35)
print(f'Lista Completa >>> {num}')
print('-'*35)
print(f'Números Pares digitados: {par}')
print(f'Números Ímpares digitados: {impar}')
