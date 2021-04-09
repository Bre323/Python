list = []
min = 0
max = 0

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1

print('-'*35)
print(f'Os valores digitados foram: {list}')
