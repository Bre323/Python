ano = int(input('Digite o ano que deseja analisar: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ANO BISSEXTO')
else:
    print('ANO NORMAL')
