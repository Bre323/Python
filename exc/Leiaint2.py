def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except(ValueError, TypeError):
            print('\033[31mERRO. DIGITE UM NÚMERO VÁLIDO\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mENTRADA DE DADOS INTERROMPIDA\033[m')
            return 0
        else:
            return num


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except(ValueError, TypeError):
            print('\033[31mERRO. DIGITE UM NÚMERO VÁLIDO\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mENTRADA DE DADOS INTERROMPIDA\033[m')
            return 0
        else:
            return num


ni = leiaint('Digite um número inteiro: ')
nf = leiafloat('Digite um número real: ')
print(f'Número inteiro: {ni} \nNúmero real: {nf:.2f}')
