def aumenta(preco=0, taxa=0):
    re = preco + (preco * taxa/100)
    return re


def diminui(preco=0, taxa=0):
    re = preco - (preco * taxa/100)
    return re


def dobro(preco=0):
    re = preco * 2
    return re


def metade(preco=0):
    re = preco / 2
    return re


def resume(preco=0, taxa=25):
    print('-'*35)
    print('RESUMO'.center(35))
    print('-'*35)
    print(f'Preço digitado: R${preco}')
    print(f'Dobro de R${preco:.2f}: R${dobro(preco):.2f}')
    print(f'Metade de R${preco:.2f}: R${metade(preco):.2f}')
    print('-'*35)
    print(f'Aumento em 25% de R${preco:.2f}: R${aumenta(preco, 25):.2f}')
    print(f'Redução em 25% de R${preco:.2f}: R${diminui(preco, 25):.2f}')
    print()
