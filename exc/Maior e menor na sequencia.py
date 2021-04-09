maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input('Peso da {}° pessoa: ' .format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso digitado >>> {}Kg' .format(maior))
print('Menor peso digitado >>> {}Kg' .format(menor))
