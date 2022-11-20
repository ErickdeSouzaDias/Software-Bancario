from conta import Conta
from criar_conta import CriarConta

usuario = Conta

while True:
    menu = str(input('''
1 - Criar Conta
opção: ''')).strip()[0]

    if menu == '1':
        CriarConta.criacao_da_conta(usuario)
