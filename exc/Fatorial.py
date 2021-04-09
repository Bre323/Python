def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
        if c > 1:
            print(' x ', end='')
        if c == 1:
            print(' = ', end='')
        f *= c
    return f


f = int(input('Digite um número para o fatorial: '))
print(fatorial(f, show=True))
