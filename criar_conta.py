from conta import Conta
from arquivo import Arquivo


class CriarConta(Conta):
    def __init__(self, nome, cpf, idade):
        Conta.__init__(self, nome, cpf, idade)

    def criacao_da_conta(self):
        self.nome = str(input('Seu nome: '))
        self.cpf = str(input('Seu CPF: '))
        self.idade = int(input('Sua idade: '))


