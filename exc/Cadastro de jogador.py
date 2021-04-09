time = list()
jogador = dict()
part = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totp = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    part.clear()
    for c in range(0, totp):
        part.append(int(input(f'   Quantos gols foram marcados na {c+1}° partida? ')))
    jogador['gols'] = part[:]
    jogador['total'] = sum(part)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Por favor, digite apenas S ou N: ')
    if r == 'N':
        break

print('-'*60)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 para sair)? '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'NÃO EXISTE JOGADOR COM CODIGO {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   - No jogo {i+1} fez {g} gols')
    print('-'*60)
print('<<< VOLTE SEMPRE >>>')
