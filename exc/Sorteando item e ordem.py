import random

p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))

people = [p1, p2, p3, p4]
escolhido = random.choice(people)
random.shuffle(people)

print('\n')
print('|'*50)
print('Aluno escolhido: {}' .format(escolhido))
print('|'*50)
print('{}\n' .format(people))
