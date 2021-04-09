matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maisc = spar = stcol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um número [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print('='*35)
print(f'A soma dos valores pares da matriz é de {spar}')
for l in range(0, 3):
    stcol += matrix[l][2]
print(f'A soma dos elementos da terceira coluna é de {stcol}')
for c in range(0, 3):
    if c == 0:
        maisc = matrix[1][c]
    elif matrix[1][c] > maisc:
        maisc = matrix[1][c]
print(f'O maior valor da segunda linha é de {maisc}')
