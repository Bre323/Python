sal = float(input('Qual o seu salário? '))

if sal > 1250:
    print('-=-'*15)
    print('Voce teve um aumento salarial de R${:.2f} >>> Salário atual = R${:.2f}'.format(sal, sal*1.1))
    print('-=-'*15)
else:
    print('-=-' * 15)
    print('Voce teve um aumento salarial de R${:.2f} >>> Salário atual = R${:.2f}'.format(sal, sal * 1.15))
    print('-=-' * 15)
