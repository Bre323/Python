def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        print(f'{idade} Anos >>> NÃO VOTA')
    elif 16 <= idade < 18 or idade >= 70:
        print(f'{idade} Anos >>> VOTO OPCIONAL')
    else:
        print(f'{idade} Anos >>> VOTO OBRIGATÓRIO')


nasc = int(input('Qual o ano de nascimento do eleitor? '))
voto(nasc)
