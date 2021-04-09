from random import randint
v = 0

while True:
    n = int(input('Digite um valor: '))
    cpu = randint(0, 10)
    tot = n + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar {P/I}? ')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador {cpu}.')
    print(f'Total: {tot}')
    print('número PAR' if tot % 2 == 0 else 'número IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Voce GANHOU')
            v += 1
        else:
            print('PERDEU')
            break
    elif tipo == 'I':
        if tot % 2 != 0:
            print('Voce GANHOU')
            v += 1
        else:
            print('PERDEU')
            break
print('GAME OVER. Voce teve {} vitorias consecutivas' .format(v))
