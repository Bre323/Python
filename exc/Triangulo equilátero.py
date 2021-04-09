lad1 = int(input('Digite o valor do primeiro lado do triangulo: '))
lad2 = int(input('Digite o valor do primeiro lado do triangulo: '))
lad3 = int(input('Digite o valor do primeiro lado do triangulo: '))

if lad1 < lad2 + lad3 and lad2 < lad1 + lad3 and lad3 < lad1 + lad2:
    print('Os valores digitados podem formar um trangulo')
    if lad1 == lad2 == lad3:
        print('O triangulo formado é EQUILÁTERO')
    elif lad1 == lad2 or lad2 == lad3 or lad3 == lad1:
        print('O triangulo formado é ISÓSCELES')
    elif lad1 != lad2 != lad3:
        print('O triangulo formado é ESCALENO')
else:
    print("IMPOSSÍVEL DE FORMAR TRIANGULO")
