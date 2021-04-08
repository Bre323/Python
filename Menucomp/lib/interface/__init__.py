def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except(ValueError, TypeError):
            print('\033[31mERRO. DIGITE UM NÚMERO VÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mENTRADA DE DADOS INTERROMPIDA\033[m')
            return 0
        else:
            return num


def lin(tam=45):
    return '-' * tam


def cab(msg):
    print(lin())
    print(msg.center(45))
    print(lin())


def menu(lst):
    cab('MENU PRINCIPAL')
    c = 1
    for i in lst:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(lin())
    op = leiaint('Sua opção: ')
    return op
