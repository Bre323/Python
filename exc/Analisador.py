somage = 0
media = 0
agemasc = 0
oldnome = ''
totmul20 = 0
for p in range(1, 5):
    print('-----{}° PESSOA-----' .format(p))
    n = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    somage += age
    if p == 1 and s in 'Mm':
        agemasc = age
        oldnome = n
    if s in 'Mm' and age > agemasc:
        agemasc = age
        oldnome = n
    if s in 'Ff' and age < 20:
        totmul20 += 1
media = somage/4
print('A média de idade do grupo é de {} anos' .format(media))
print('O nome do homem mais velho do grupo é {} e tem {} anos de idade' .format(oldnome, agemasc))
print('Existem {} mulheres com menos de 20 anos nesse grupo' .format(totmul20))
