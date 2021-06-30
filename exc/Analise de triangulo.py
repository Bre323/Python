a = int(input('Digite a primeira medida do triangulo: '))
b = int(input('Digite a segunda medida do triangulo: '))
c = int(input('Digite a terceira medida do triangulo: '))

if a < b + c and b < a + c and c < a + b:
    print('As medidas podem formar um triangulo!!')
else:
    print('ERRO')
    print('IMPOSSIVEL FORMAR UM TRIANGULO')
