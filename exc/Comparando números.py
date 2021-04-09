num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num > num2:
    print('\nO primeiro número ({}) é maior que o segundo número ({})' .format(num, num2))
elif num == num2:
    print('\nOs Dois números são equivalentes!!!')
else:
    print('\nO primeiro número ({}) é menor que o segundo número ({})' .format(num, num2))
