from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
rank = dict()
for k, v in jogo.items():
    print(f'Dado do {k} >>>  {v}')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('='*30)
for i, v in enumerate(rank):
    print(f' O {i+1}° lugar ficou com {v[0]} que tirou {v[1]}')
