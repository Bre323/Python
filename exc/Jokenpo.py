from random import randint

item = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)

print('''Suas opções:
[1]PEDRA
[2]PAPEL
[3]TESOURA
''')
player = int(input('Escolha uma das opções: '))
itplayer = player-1

print('\nComputador escolheu {}' .format(item[cpu]))
print('\nVoce escolheu {}\n' .format(item[itplayer]))
print('='*25)

if cpu == 0:
    if itplayer == 0:
        print('EMPATE')
    elif itplayer == 1:
        print('VOCE GANHOU')
    elif itplayer == 2:
        print('VOCE PERDEU')
    else:
        print('PARTIDA INVÁLIDA. TENTE NOVAMENTE')
elif cpu == 1:
    if itplayer == 0:
        print('VOCE PERDEU')
    elif itplayer == 1:
        print('EMPATE')
    elif itplayer == 2:
        print('VOCE VENCEU')
    else:
        print('PARTIDA INVÁLIDA. TENTE NOVAMENTE')
elif cpu == 2:
    if itplayer == 0:
        print('VOCE VENCEU')
    elif itplayer == 1:
        print('VOCE PERDEU')
    elif itplayer == 2:
        print('EMPATE')
    else:
        print('PARTIDA INVÁLIDA. TENTE NOVAMENTE')
else:
    print('PARTIDA INVÁLIDA. TENTE NOVAMENTE')
