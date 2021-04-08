tot18 = toth = totm20 = 0
while True:
    age = int(input('Digite sua idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        toth += 1
    if sex == 'F' and age < 20:
        totm20 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total de pessoas maiores de 18: {tot18}')
print(f'Total de pessoas do sexo masculino: {toth}')
print(f'Total de Mulheres abaixo de 18: {totm20}')
