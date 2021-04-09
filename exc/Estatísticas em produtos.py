tot = pmil = prbar = cont = 0
nbar = ' '
while True:
    prod = str(input('\nNome do produto: '))
    prec = float(input('Preço: R$ '))
    tot += prec
    cont += 1
    if prec > 1000:
        pmil += 1
    if cont == 1 or prec < prbar:
        prbar = prec
        nbar = prod
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'\nTotal Gasto: R${tot:.2f}')
print(f'{pmil} produtos possuem mais de 1000 reais')
print(f'O produto mais barato foi {nbar} que custa {prbar:.2f}')
