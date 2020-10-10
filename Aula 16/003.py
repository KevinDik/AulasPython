class Elevador:

    def __init__(self):
        andar = totandares = capacidade = pessoas = 0
        self.__andar = andar
        self.__totandares = totandares
        self.__capacidade = capacidade
        self.__pessoas = pessoas
        print(f'Elevador inicializando com sucesso')

    def inicializa(self, capacidade_inicial, totandares_inicial):
        """
        inicia o elevador de acordo com os parametros
        :param capacidade_inicial: capacidade total de peso do elevador
        :param totandares_inicial: total de andares do predio
        :return:
        """
        self.__capacidade = capacidade_inicial
        self.__totandares = totandares_inicial
        print(f'andar atual: {self.__andar}, total de andares: {self.__totandares}, capacidade {self.__capacidade}, pessoas: {self.__pessoas}')

    def entra(self, pessoa):
        """
        adiciona pessoas ao elevador
        :param pessoa: numero de pessoas adicionadas
        :return:
        """
        if pessoa > self.__capacidade:
            print(f'Elevador com limite atingido {self.__capacidade} pessoas no elevador')
        else:
            self.__pessoas += pessoa
            print(f'{self.__pessoas} pessoa(as) entrou(aram) no elevador')

    def sai(self, pessoa):
        """
        retira pessoas do elevador
        :param pessoa: numero de pessoas que sairao
        :return:
        """
        if pessoa == 0:
            print(f'Não é possivel sair ninguem pois o elevador está vazio')
        else:
            if self.__pessoas - pessoa < 0:
                print('Não é possivel sair pessoas menores que zero')
            else:
                self.__pessoas -= pessoa
                print(f'{pessoa} pessoa(s) saiu(ram), total de pessoas no elevador {self.__pessoas}')

    def sobe(self, valor):
        """
        sobe para o andar selecionado
        :param valor: numero do andar
        :return:
        """
        if valor > self.__totandares or valor < 0:
            print(f'Você está no {self.__andar} andar, so é permitido descer')
        else:
            self.__andar = valor
            print(f'Elevador subindo para o andar: {self.__andar}')

    def desce(self, valor):
        """
        desce para o andar selecionado
        :param valor: numero do andar destino
        :return:
        """
        if self.__andar - valor < 0:
            print(f'Não é possivel descer para um andar maior ou igual que o andar. Atual {self.__andar} andar')
        else:
            self.__andar = valor
            if self.__andar < 0:
                print('Não é permitido numeros negativos')
            else:
                print(f'Descedo para o andar {self.__andar}')


#Programa principal
el = Elevador()
el.inicializa(5, 10)
#el.entra(4)
#el.sai(4)
el.sobe(7)
el.desce(4)
