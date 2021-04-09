frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inv = ''

for let in range(len(junto) - 1, -1, -1):
    inv += junto[let]
print('O inverso de {} é {}' .format(junto, inv))
if inv == junto:
    print('PALÍNDROMO')
else:
    print('Não é palíndromo')
