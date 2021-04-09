peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)

print('O IMC é de {}' .format(imc))
if imc < 18.5:
    print('Voce está ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Voce está No PESO IDEAL')
elif 25 <= imc < 30:
    print('Voce está no SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está OBESO')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
