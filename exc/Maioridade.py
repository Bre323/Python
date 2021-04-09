from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1, 8):
    nasc = int(input('Qual o ano em que a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Pessoas na MAIORIDADE: {}' .format(totmaior))
print('Pessoas menores de idade: {}' .format(totmenor))
