aluno = {}
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'

print('='*30)
for k, v in aluno.items():
    print(f'{k} >>> {v}')
