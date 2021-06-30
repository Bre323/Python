class computer:
    def __init__(self, marca, ram, placavideo, processador):
        self.marca = marca
        self.ram = ram
        self.placavideo = placavideo
        self.processador = processador

    def ligar(self):
        print('Ligado!!')
    def desligar(self):
        print('Desligado!!')
    def mostrarmarca(self):
        print(f'Marca do computador: {self.marca}')
    def exibirinfo(self):
        print(f'Memoria RAM: {self.ram}')
        print(f'Placa de Video: {self.placavideo}')
        print(f'Processador: {self.processador}')

computer1 = computer('Asus', '8gb', 'Nvidia', 'Intel i9')
computer2 = computer('Positivo', '8gb', 'Gigabyte', 'intel')
computer3 = computer('Alienware', '16gb', 'Geforce 3080', 'intel i9 10°gen')

com = int(input('Selecione o computador: '))
if com == 1:
    com = computer1
if com == 2:
    com = computer2
if com == 3:
    com = computer3
else:
    print('ERRO. Digite 1, 2 ou 3:    ')

while True:

    print('-'*40)
    print(' '*18, ' MENU', ' '*18)
    print('-'*40)
    print()
    print('1 - Ligar')
    print('2 - Desligar')
    print('3 - Exibir marca')
    print('4 - Exibir info')
    print('5 - Sair do Programa')
    op = int(input('\nSelecione uma das opções: '))

    if op == 1:
        computer.ligar(com)
    if op == 2:
        computer.desligar(com)
    if op == 3:
        computer.mostrarmarca(com)
    if op == 4:
        computer.exibirinfo(com)
    if op == 5:
        break
