s = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c
        cont += 1
print('\n\nA soma de todos os {} valores impares divisíveis por 3 entre 1 e 500 é igual a {}' .format(cont, s))
