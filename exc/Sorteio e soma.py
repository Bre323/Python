from random import randint
from time import sleep


def sorteio(lista):
    print('SORTEANDO 5 VALORES PARA A LISTA: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.25)
    print('\nFIM\n')


def sompar(lista):
    s = 0
    for val in lista:
        if val % 2 == 0:
            s += val
    print(f'Somando todos os valores pares da lista temos {s}')


nums = list()
sorteio(nums)
sompar(nums)
