'''
Metodos (funcoes)
representam os comportamentos dos objetos, as acoes que esse objeto pode realizar no sistema

Em python dividimos os metodos assim como os atributos em dois grupos
metodos de instancia/metodos de classe

#metodos de instancia

metodo dunder init __init__ e um metodo especial chamado construtor e sua funcao e construir o objeto

obs todo elemento em pyton que inicia e finaliza com __ e chamado de dunder (double underline)

Os metodos dunder em pyhton sao chamados de metodos magicos
por mais que se possa criar nossas proprias funcoes utilizando dunder nao e aconselhado, python possui metodos com essa forma e pode ser que mudemos o comportamento dessas
funcoes magicas internas

metodos sao escritos em letras minusculas

p1 = Produto('playstation', 'video game', 2300)
print(Produto.desconto(p1, 40)) # self, desconto

user1 = Usuario('kevin', 'diego', 'kdss@gmail.com', '123')
user2 = Usuario('michelly', 'amaral', 'ma@gmail.com', '456')

print(user1.nome_completo())
print(user2.nome_completo())

print(Usuario.nome_completo(user1))



#print(f'senha {user1._Usuario__senha}') # acesso de forma errada
#print(f'senha {user2._Usuario__senha}')

nome = input('Informe o nome')
sobrenome = input('informe o sobrenome')
email = input('Informe o email')
senha = input('Informe sua senha')
confirma_senha = input('confirma senha?')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha nao confere')
    exit(1)

print('Usuario criado com sucesso')

senha = input('informe a senha para acesso')
if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'senha criptografada {user._Usuario__senha}') #acesso errado

metodos de classe em python sao conhecidos como estaticos em outras linguagens

#metodos de classe
user = Usuario('kevin', 'diego', 'kevindiego@gmail.com', '226921')
user2 = Usuario('michelly', 'Amaral', 'michellyamaral@gmail.com', '2269211')

Usuario.conta_usuario() #forma correta
user.conta_usuario() #forma incorreta



user = Usuario('felicity', 'jhons', 'kdss@gmail.com', '123456')
#print(user.__gera_usuario()) # Erro de atributo
#print(user._Usuario__gera_usuario()) # é possivel porem de forma errada

'''
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada():
    def __init__(self, cor, voltagem, luminosidade):
        self.___cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente():
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto():
    contador = 0

    def __init__(self, nome, decricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = decricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """
        retorna o valor do produto com desconto
        :param porcentagem:
        :return:
        """
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario():
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('teste')  # se nao tiver envolvido com nenhuma instancia mas tivem com classe ele tem que ser static

    @staticmethod
    def deficicao(): #metodo estatico, nao tem acesso a classe e nem a instancia
        return 'kdss226921'


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # gera uma criptografia para senha
        Usuario.contador = self.__id
        print(f'Usuario criado {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):  # criacao de metodo privado
        return self.__email.split('@')[0]


#metodo estatico

print(Usuario.contador)
print(Usuario.deficicao())
user = Usuario('kevin', 'diego', 'kevindiego@gmail.com', '226921')
print(user.contador)
print(user.deficicao())