class Pessoa:
    dicionario = {}
    lista = []
    
    def __init__(self, nome, idade, altura):
        """
        metodo construtor para uma pessoa
        :param nome: nome do individuo
        :param idade: sua idade
        :param altura: sua altura
        """
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Pessoa.dicionario = {'nome': self.__nome, 'idade': self.__idade, 'altura': self.__altura}
        Pessoa.lista.append(Pessoa.dicionario.copy())

    @classmethod
    def imprime_agenda(cls):
        """
        imprime as pessoas
        :return: realiza uma impressao de todas as pessoas na lista descrita com nome idade e altura
        """
        for valor in Pessoa.lista:
            print(f'nome: {valor["nome"]}, idade: {valor["idade"]} anos, altura: {valor["altura"]} metros')


    @classmethod
    def remover_pessoa(cls, nome):
        """
        remove a pessoa de acordo com o nome dado como parametro
        :param nome: nome a ser removido
        :return:
        """
        for valor in Pessoa.lista:
            if nome == valor['nome']:
                print(f'A pessoa {valor["nome"]} foi removida com suesso')
                Pessoa.lista.remove(valor)
            else:
                print(f'Nome {nome} não localizado na agenda')
                break

    @classmethod
    def localiza_pessoa(cls, nome):
        """
        localiza a posicao da pessoa dentro da lista e imprime sua posicao
        :param nome: nome como parametro
        :return:
        """
        for posicao, valor in enumerate(Pessoa.lista):
            if nome == valor['nome']:
                print(f'A pessoa {valor["nome"]} esta localizada no item {posicao}')
            else:
                print(f'Nome {nome} não localizado na agenda')
                break
    @classmethod
    def imprime_pessoa(cls, numero):
        """
        localiza a pessoa na lista de acordo com o numero de posicao e imprime seus dados
        :param numero: numero da posicao
        :return:
        """
        try:
            print(f'nome {Pessoa.lista[numero]}')
        except TypeError:
            print('Valor inserido não é um número')
        except IndexError:
            print('Número inserido no metodo não corresponde a um local na agenda')


# Programa
pessoa = Pessoa('kevin', 25, 1.89)
pessoa2 = Pessoa('diego', 13, 1.45)
pessoa3 = Pessoa('michelly', 25, 1.55)
pessoa4 = Pessoa('carlos', 41, 1.78)
pessoa5 = Pessoa('davi', 10, 1.15)
pessoa6 = Pessoa('tatiana', 29, 1.65)
pessoa7 = Pessoa('wemerson', 27, 1.64)
pessoa8 = Pessoa('welton', 45, 1.25)
pessoa9 = Pessoa('michel', 32, 1.78)
pessoa10 = Pessoa('lucas', 14, 1.90)

pessoa.imprime_agenda()
print('*' * 30)
pessoa.remover_pessoa(45)
