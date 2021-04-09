from datetime import date

ano = int(input('ano de nascimento: '))
idade = date.today().year - ano

print('='*80)
if idade <= 9:
    print('Voce tem {} anos' .format(idade))
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Voce tem {} anos' .format(idade))
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: JÚNIOR')
elif idade <= 24:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: SÊNIOR')
else:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: MASTER')
print('='*80)
