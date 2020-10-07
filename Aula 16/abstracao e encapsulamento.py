'''
O grande objetivo da poo e encapsular o codigo dentro de um grupo logico e hierarquico utilizando classes

# atributos/metodos privados em python
uma classe pessoa contendo um atributo privado chamado __nome, e metodo privado chamado __falar
esses elementos privados so deveriam ser acessados dentro da classe, mas python nao bloqueia este acesso fora da classe.
com python acontece um fenomeno chamado name mongling que faz uma alteracao na forma de se acessar os elementos privados
conforme _classe__elemento

Exemplos de acesso:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstracao é o ato de expor apenas dados relevantes de uma classe escondendo atributos e metodos privados de usuario

#teste
conta1 = Conta('kevin', 150, 1500)


print(conta1.__dict__)
conta1.extrato()

conta1._Conta__titular = 'xuxa' nao se deve realizar assim, porem e perimitido
print(conta1.__dict__)


conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(-200)

print(conta1.__dict__)
'''


class Conta():
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'Valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('valor tem que ser positivo')

    def transferir(self, valor, conta_desitno):
        #   remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferencia paga por quem realizou a transferencia
        #   adcionar o valor na conta de destino
        conta_desitno.__saldo += valor


conta1 = Conta('kevin', 150, 1500)
print(conta1.__dict__)
conta2 = Conta('diego', 300, 2000)
print(conta2.__dict__)

conta2.transferir(100, conta1)
print(conta1.__dict__)
print(conta2.__dict__)

