num = int(input('Digite um número inteiro: '))
print('Selecione uma base numérica para a conversão:')
print('\n[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal\n')
opt = int(input('Sua opção: '))

if opt == 1:
    print('O valor inteiro {} em Binário é {}' .format(num, bin(num)[2:]))
elif opt == 2:
    print('O valor inteiro {} em Octal é {}' .format(num, oct(num)[2:]))
elif opt == 3:
    print('O valor inteiro {} em Hexadecimal é {}' .format(num, hex(num)[2:]))
else:
    print('ERROR')
