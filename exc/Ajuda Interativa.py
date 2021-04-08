cor = ('\033[m',             # Sem cor
       '\033[0;30;41m',      # Vermelho
       '\033[0;30;42m',      # Verde
       '\033[0;30;43m',      # Amarelo
       '\033[0;30;44m')      # Azul


def ajuda(com):
    print(cor[4], end='')
    help(com)
    print(cor[0], end='')


com = ''
while True:
    com = str(input('Digite uma função/biblioteca: '))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
print(cor[1], end='')
print('<<< VOLTE SEMPRE >>>')
print(cor[0])
