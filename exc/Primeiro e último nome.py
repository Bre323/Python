nome = str(input('Digite o nome completo: ')).strip().split()

print('-'*50)
print('Primeiro nome: {}' .format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))
print('-'*50)
