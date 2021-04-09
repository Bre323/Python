def leiaint(msg):
    ok = False
    val = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            val = int(n)
            ok = True
            break
        else:
            print('\033[0;31mVALOR INVALIDO. DIGITE UM NÚMERO\033[m')
        if ok:
            break
    return val

n = leiaint('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
