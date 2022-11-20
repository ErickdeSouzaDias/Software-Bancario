from criar_conta import CriarConta
arquivo = open('lista de clientes.json', 'a')


class Arquivo(CriarConta):
    def __init__(self, nome, cpf, idade):
        CriarConta.__init__(self, nome, cpf, idade)

    def adicionacliente(self):
        clientes = {
            'Nome': f'{self.nome}',
            'CPF': f'{self.cpf}',
            'Idade': f'{self.idade}',
        }

        arquivo.write(str(clientes))
