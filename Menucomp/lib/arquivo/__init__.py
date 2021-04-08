from Menucomp.lib.interface import *

def verifarq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO NA CRIAÇÃO DE ARQUIVO')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER ARQUIVO')
    else:
        cab('PESSOAS CADASTRADAS')
        for li in a:
            dado = li.split(',')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>10} anos')
    finally:
        a.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO AO ABRIR O ARQUIVO')
    else:
        try:
            a.write(f'{nome}, {idade}\n')
        except:
            print('HOUVE UM ERRO AO ESCREVER DADO NO ARQUIVO')
        else:
            print('NOVO REGISTRO ADICIONADO')
            a.close()
