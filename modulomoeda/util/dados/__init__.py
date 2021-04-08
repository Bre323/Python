def leitura(msg):
    valida = False
    while not valida:
        inp = str(input(msg)).replace(',', '.').strip()
        if inp.isalpha() or inp == '':
            print(f'\033[0;31mERRO. \"{inp}\" É INVÁLIDO\033[m')
        else:
            valida = True
            return float(inp)


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
