while True:
    n = int(input('Voce quer ver a tabuada de qual número? '))
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
        c -= 1
    print('-'*30)
    if n == 0:
        break
print('FIM')
