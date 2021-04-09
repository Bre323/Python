dist = float(input('Digite a distancia da viagem: '))
dc = dist*0.5
dl = dist*0.45

if dist > 200:
    print('-'*50)
    print('Custo de viagem >>> R${:.2f}'.format(dl))
    print('-'*50)
else:
    print('-'*50)
    print('Custo de viagem >>> R${.:2f}'.format(dc))
    print('-'*50)
