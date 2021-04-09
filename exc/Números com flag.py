som = cont = 0
while True:
    n = int(input('Digite um número (999 para sair do programa): '))
    if n == 999:
        break
    som += n
    cont += 1
print(f'Foram digitados {cont} números e a soma entre todos eles é igual a {som}')
