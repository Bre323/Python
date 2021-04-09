from datetime import datetime
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Número da Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aponsentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('='*35)
for k, v in dados.items():
    print(f'- {k}: {v}')
