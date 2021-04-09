from math import trunc

num = float(input('Digite um número real: '))
nint = trunc(num)

print('-'*50)
print('O número digitado foi {}, e a porção inteira é {}' .format(num, nint))
print('-'*50)

''' 
Print('O número digitado foi {}, e a porção inteira é {}' .format(num, int(num)))
'''
