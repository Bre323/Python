listnum = []
numin = 0
numax = 0

for c in range(0, 5):
    listnum.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        numin = numax = listnum[c]
    else:
        if listnum[c] > numax:
            numax = listnum[c]
        if listnum[c] < numin:
            numin = listnum[c]
print('='*35)
print(f'Lista = {listnum}')
print('='*35)
print(f'O menor número digitado foi {numin} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == numax:
        print(f'{i}... ', end='')
print()
print(f'O maior número digitado foi {numax} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == numin:
        print(f'{i}... ', end='')
print()
