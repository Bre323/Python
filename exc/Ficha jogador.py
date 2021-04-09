def ficha(jogador='<unknown>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s)')


nome = str(input('Digite o nome do jogador: '))
gol = str(input(f'Quantos gols o jogador fez? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)
