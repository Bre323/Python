n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0

while op != 7:
    print('''[1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Maior
    [6] Novos números
    [7] Sair do programa''')
    op = int(input('\nEscolha uma opção >>>> '))

    if op == 1:
        print('O resultado da soma entre {} e {} é {}' .format(n1, n2, n1+n2))
    elif op == 2:
        print('O resultado da subtração entre {} e {} é {}'.format(n1, n2, n1-n2))
    elif op == 3:
        print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif op == 4:
        print('O resultado da divisão entre {} e {} é {}'.format(n1, n2, n1/n2))
    elif op == 5:
        if n1 > n2:
            print('O primeiro número ({}) é MAIOR do que o segundo número ({})' .format(n1, n2))
        elif n1 < n2:
            print('O primeiro número ({}) é MENOR do que o segundo número ({})' .format(n1, n2))
        else:
            print('SÃO IGUAIS')
    elif op == 6:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 7:
        print('FINALIZANDO O PROGRAMA......')
    else:
        print('Comando inválido')
