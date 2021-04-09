r = 'S'
som = med = quant = maior = menor = 0

while r in 'Ss':
    num = int(input('Digite um número: '))
    som += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]

med = som / quant
print('Voce digitou {} números e a média é {}'.format(quant, med))
print('O maior número foi {} e o menor número foi {}' .format(maior, menor))
print('FIM')
