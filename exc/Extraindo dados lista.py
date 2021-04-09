nums = []

while True:
    nums.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N]  '))
    if op in 'Nn':
        break

print('-'*35)
print(f'Voce digitou {len(nums)} números')
nums.sort(reverse=True)
print(f'{nums}')
print('5 está na lista' if 5 in nums else 'O número 5 não faz parte da lista')
