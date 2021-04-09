dados = []
pessoas = []
men = mai = 0

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    if len(pessoas) == 0:
        men = mai = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break
print('-'*35)
print(f'Foram cadastrados {len(pessoas)} pessoas na lista')
print('-'*35)
print(f'A pessoa mais pesada cadastrada possui {mai}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'A pessoa mais leve cadastrada possui {men}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
