valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos_pagamento = int(input('Digite o período de pagamento da casa: '))
prest_mensal = valor_casa / (anos_pagamento*12)

print('='*80)
print('A prestação mensal a ser paga é de R${:.2f}' .format(prest_mensal))
if prest_mensal <= salario*0.3:
    print('Empréstimo Aprovado >>> R${:.2f} a ser pago em {} anos' .format(valor_casa, anos_pagamento))
else:
    print('\nEmpréstimo NEGADO')
    print('O valor ultrapassa 30% do seu salário')
print('='*80)
