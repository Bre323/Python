from random import randint

numcpu = randint(0, 10)
n = int(input('Pensei em um número. Tente adivinhar'))
adv = 0

while n != numcpu:
    if n < numcpu:
        n = int(input('É maior. Tente adivinhar: '))
    else:
        n = int(input('È menor. Tente adivinhar: '))
    adv += 1
print('O número certo é {} >>> Voce tentou adivinhar {} vezes' .format(numcpu, adv))
