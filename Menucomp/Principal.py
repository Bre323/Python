from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'list.txt'
if not verifarq(arq):
    criarquivo(arq)

while True:
    re = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if re == 1:
        lerarquivo(arq)
    elif re == 2:
        cab('CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastro(arq, nome, idade)
    elif re == 3:
        cab('>>> VOLTE SEMPRE <<<')
        break
    else:
        print('\033[31mERRO. DIGITE UMA OPÇÃO VÁLIDA\033[m')
        sleep(1)
