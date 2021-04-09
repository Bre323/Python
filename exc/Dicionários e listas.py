pessoa = dict()
grupo = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite apenas M ou F: ')
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Por favor, digite apenas S ou N')
    if r == 'N':
        break
media = soma/len(grupo)

print('='*60)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas')
print(f'B) A média de idade das pessoas cadastradas é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ')
for p in grupo:
    if p['sexo'] == 'F':
        print('    ', end='')
        print(f'-> {p["nome"]}')
print(f'D) As pessoas com a idade acima da media são: ')
for p in grupo:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'-> {k} = {v};', end=' ')
        print()
print('<<<FINALIZADO>>>')
