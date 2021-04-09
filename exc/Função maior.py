from time import sleep

def maior(* n):
    cont = mai = 0
    print('='*30)
    print('ANALISANDO VALORES')
    for val in n:
        print(f'{val}', end='  ')
        sleep(0.25)
        if cont == 0:
            mai = val
        else:
            if val > mai:
                mai = val
        cont += 1
    print(f'Ao todo foram {len(n)} valores')
    print(f'O maior valor encontrado foi {mai}')


maior(3, 5, 7, 8, 4, 9)
maior(9, 6, 3)
maior(0)
maior(3, 5)
maior(9, 6, 3, 5)
