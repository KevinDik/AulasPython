"""
Atributos representam as caracteristicas do objeto. Ou seja pelos atributos conseguimos representar
computacionalmente os estados dos objetos

Em python exitem 3 grupos de atributos
atributo de instancia
atributo de classe
atributo dinamicos

Atributo de instância
São atributos declarados dentro do metodo construtor (metodo especial utilizado para criar a construcao do obj)

Em pyhton por convencao ficou estabelecido que todo atributo de uma classe é publico
caso queira que deve ser tratado como privado utiliza-se duplo underscore __ no inicio no seu nome
conhecido como Name Mangling

# classes com atributo de instancia publico


# obs: isso é apenas uma convencao, a linguagem nao vai impedir acesso dos atribuos sinalizados
user = Acesso('user@gmail.com', '123')
print(user.email)
#print(user.__senha) atribuite error
print(user._Acesso__senha) # tem acesso mas não deve
user.MostraSenha()
user.MostraEmail()

# Atributos de instancia
# ao criarmos instancias de uma classe todas as instancias terao estes atributos

user1 = Acesso('user@gmail.com', '456')
user2 = Acesso('user2@gmailcom', '789')

user1.MostraEmail()
user2.MostraEmail()

#Atributos de classe


p1 = Produto('playstation', 'videogame', 2399)
p2 = Produto('Xbox', 'videogame', 4399)
# São atributos que são declarados diretamente na classe, fora do construtor. Geralmente inicializamos um valor
# valor é compartilhado entre todas as instancias da classe, ao invez de casa instancia ter seus proprios valores
# todas as instancias terao o mesmo valor para este atributo

p3 = Produto('playstation 4', 'videogame', 2300)
p4 = Produto('xbox 5', 'videogame', 4500)

print(p3.valor) #acesso possivel mas incorreto
print(p4.valor) #acesso possivel mas incorreto

# obs nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto) # mostra o imposto do Produto. Acesso correto
print(p3.id)
print(p4.id)

# obs em java os atributos de classe no pyhton sao os statics
"""
class Lampada:
    def __init__(self, voltagem, cor): #metodo construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo): #metodo construtor
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Teste:
    def __init__(cerveja, nome, idade): #primeiro parametro de um metodo é o self. Proprio objeto. Mas o self pode ser renomeado
        cerveja.nome = nome
        cerveja.idade = idade


#Atributos publicos e privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def MostraSenha(self):
        print(self.__senha)

    def MostraEmail(self):
        print(self.email)




class Produto:
    imposto = 1.05 #atibuto estatico
    contador = 0 #atributo estatico

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id

#Atributo dinamico
#um atributo de instancia que pode ser criado em tempo de execução
#Atributo dinamico será exclusivo da instancia que o criou


p1 = Produto('playstation 4', 'videogame', 2300)
p2 = Produto('arroz', 'mercearia', 5.99)

#criando um atributo dinamico em tempo de execucao

p2.peso = '5kg'

print(f'Produto: {p2.nome}, descricao: {p2.descricao}, valor: {p2.valor}, peso: {p2.peso}')
print(f'Produto: {p1.nome}, descricao: {p1.descricao}, valor: {p1.valor}, peso: {p1.peso}') # Erro pois nap tem o atributo

# deletando atributos

print(p1.__dict__)
print(p2.__dict__)

print(Produto.__dict__)

del p2.peso #apaga o atributo peso
