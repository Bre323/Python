preco = float(input('Preço das compras >> R$'))
print('''Formas de Pagamento
[1] à vista no dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opt = int(input('Sua opção: '))

if opt == 1:
    total = preco * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f}' .format(preco, total))
elif opt == 2:
    total = preco * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f}' .format(preco, total))
elif opt == 3:
    print('Sua compra de R${:.2f} foi dividida em parcelas de R${:.2f}' .format(preco, (preco/2)))
elif opt == 4:
    total = preco + preco*0.2
    parc = int(input('Quantas parcelas? '))
    prpar = total / parc
    print('Sua compra de R${:.2f} com 20% de juros custará R${:.2f}' .format(preco, total))
    print('Parcelando em {:.2f} vezes custará R${:.2f}' .format(parc, prpar))
else:
    print('Opção inválida: Preço final de R${:.2f}' .format(preco))
