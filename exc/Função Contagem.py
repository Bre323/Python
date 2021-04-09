from time import sleep

def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        print('A CONTAGEM NÃO É FEITA COM PASSO 0')
        return 0

    print('-'*50)
    print(f'CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}')
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end='  ')
            c += p
            sleep(0.25)
    else:
        c = i
        while c >= f:
            print(f'{c}', end='  ')
            c -= p
            sleep(0.25)
    print()



contagem(1, 10, 1)
contagem(10, 0, 2)
print('>>> Contagem personalizada <<<')
i = int(input('Inicio da contagem: '))
f = int(input('Final da contagem: '))
p = int(input('Passo da contagem: '))
contagem(i, f, p)
