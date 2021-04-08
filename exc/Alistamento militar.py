from datetime import date

anatual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = anatual - ano
alis = ano + 18

print('Quem nasceu em {} tem {} anos em {}' .format(ano, idade, anatual))
print('='*80)
if idade == 18:
    print('Voce precisa se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Falta {} anos para o alistamento militar' .format(alis - anatual))
    print('Seu alistamento será em {}' .format(alis))
else:
    print('Voce já deveria ter se alistado a {} anos' .format(anatual - alis))
    print('Seu ano de alistamento foi em {}' .format(alis))
print('='*80)
