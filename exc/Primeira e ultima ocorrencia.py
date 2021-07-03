frase = str(input('Digite uma frase completa: ')).lower().strip()

print('-'*50)
print('Quantidade de letras A: {}'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')+1))
print('')
print('-'*50)
