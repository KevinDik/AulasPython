class Pessoa():
    def __init__(self, nome, idade, altura):
        """
        construtor para pessoa
        :param nome: nome da pessoa
        :param idade: sua idade
        :param altura: sua altura
        """
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def mostra_dados(self):
        """
        Mostra os dados de cada pessoa
        :return: mostra formatado todos os dados
        """
        return print(f'Pessoa: {self.__nome}, tem a idade de: {self.__idade} anos, e possui {self.__altura} metros')


# Programa principal

p1 = Pessoa('Kevin', 25, 1.79)
p1.mostra_dados()
