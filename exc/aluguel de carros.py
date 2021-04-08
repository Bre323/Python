n = int(input('Digite quantos kilometros o carro percorreu: '))
d = int(input('Por quantos dias o carro será alugado? '))

kr = 0.15*n
dt = 60*d
vt = kr + dt

print('-'*50)
print('Valor total: {}' .format(vt))
print('-'*50)
