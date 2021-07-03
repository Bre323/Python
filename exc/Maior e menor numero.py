a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#ANALISANDO MENOR NÚMERO
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#ANALISANDO MAIOR NÚMERO
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

print('='*50)
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
