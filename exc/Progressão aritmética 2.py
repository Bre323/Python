print('===== Progressão aritmética =====')
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da Progressão aritmética: '))
cont = 1
t = pri
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} >>> ' .format(t))
        t += raz
        cont += 1
    mais = int(input('Quantos termos voce deseja ter mais? '))
print('\nFIM')
