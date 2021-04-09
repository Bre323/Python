ficha = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-'*30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, n in enumerate(ficha):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}')
print()

while True:
    op = int(input('Mostrar notas de qual aluno (999 para finalizar)? '))
    if op == 999:
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
print('<<<VOLTE SEMPRE>>>')
