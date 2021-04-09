from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Valores sorteados: {n}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
