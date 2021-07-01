money = float(input('Tens quanta grana? R$'))

dolar = money/3.92
euro = money/4.32
yene = money/0.037

print('-'*50)
print('É possivel comprar com {} reais:' .format(money))
print('\n{:.2f} Dólares' .format(dolar))
print('{:.2f} Euros' .format(euro))
print('{:.2f} Yene' .format(yene))
print('-'*50)
