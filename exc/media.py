n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
media = (n1+n2+n3+n4)/4

print('='*50)
print('A media das notas é de {:.2f}' .format(media))
if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('Voce está de RECUPERAÇÃO')
elif media >= 7:
    print('VOCE FOI APROVADO!!!')
print('='*50)
