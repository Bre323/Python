nums = []

while True:
    n = int(input('Digite um número para compor a lista: '))
    if n not in nums:
        nums.append(n)
        print('Valor adicionado!')
    else:
        print('Proibido adicionar valores duplicados!')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

print('='*35)
nums.sort()
print(f'Voce adicionou os valores {nums}')
