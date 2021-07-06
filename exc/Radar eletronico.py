vel = float(input('A que velocidade o carro está andando? '))
excesso = (vel - 80)*7

if vel > 80:
    print('VOCE ULTRAPASSOU O LIMITE DE VELOCIDADE')
    print('-=-'*15)
    print('Velocidade: {}'.format(vel))
    print('MULTA DE R${:.2f} reais'.format(excesso))
    print('-=-'*15)
else:
    print('Ta tudo tranquilo, pode seguir')
