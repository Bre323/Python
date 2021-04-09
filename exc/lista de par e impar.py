listcomp = []
listpar = []
listimpar = []
par = impar = 0

for c in range(0, 7):
    n = int(input('Digite um número: '))
    listcomp.append(n)
    if n % 2 == 0:
        listpar.append(n)
        par += 1
    elif n % 2 == 1:
        listimpar.append(n)
        impar += 1

listcomp.sort()
listpar.sort()
listimpar.sort()
print('-'*35)
print(f'Lista Completa >>> {listcomp}')
print(f'Foi digitado {par} números pares e {impar} números ímpares')
print('-'*35)
print(f'Lista com números pares: {listpar}')
print(f'Lista com números ímpares: {listimpar}')
