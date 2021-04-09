from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('-'*50)
print('O angulo {} tem o seno de {:.2f}' .format(ang, seno))
print('O angulo {} tem o cosseno de {:.2f}' .format(ang, cosseno))
print('O angulo {} tem a tangente de {:.2f}' .format(ang, tangente))
print('-'*50)
