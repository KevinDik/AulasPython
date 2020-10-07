'''
obejetos sao instancias da classe. Apos o mapeamento do mundo real na sua
representacao computacional. Devemos poder criar quantos objetos forem necessarios
podemos pensar nos onjetos/intancias como variaveis do tipo definido na classe

# teste
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()


cc1 = ContaCorrente(5000, 20000)

user = Usuario('kevin', 'Diego', 'kevindiego@gmail.com', '226921')

print(f'A lamprada está ligada? {lamp1.checa_lampada()}')

#teste2
nome = 'keivn'
sobrenome = 'diego'
email = 'teste'
senha = '123'

user = Usuario(nome, sobrenome, email, senha)

print(type(user))
'''


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = False

    def checa_lampada(self):
        return self.__ligado

    def ligar_desligar(self):
        if self.__ligado:
            self.__ligado = False
        else:
            self.__ligado = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrnome = sobrenome
        self.__email = email
        self.__senha = senha


cli = Cliente('kevin', '05745749300')
conta = ContaCorrente(5000, 10000, cli)

conta.mostra_cliente()

conta._ContaCorrente__cliente.diz() #acesso de forma errada atrave de metodos
