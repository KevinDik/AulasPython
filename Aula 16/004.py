class Televisao:
    def __init__(self, volume, canal):
        self.volume = volume
        self.canal = canal


class ControleRemoto:

    def __init__(self, volume, canal):
        self.__volume = volume
        self.__canal = canal

    def aumentar_volume(self):
        self.__volume += 1
        return print(f'Aumentando o volume  para {self.__volume}')

    def diminuir_volume(self):
        self.__volume -= 1
        return print(f'Diminuindo o volume para {self.__volume}')

    def canal(self, valor=1):
        if valor == 1:
            self.__canal += 1
        else:
            self.__canal = valor
        return print(f'Mudando do canal {tv.canal} para {self.__canal}')

    def consultar_valor_volume(self):
        return print(f'Volume: {self.__volume}\nCanal: {self.__canal}')


#teste
tv = Televisao(5, 10)
print(tv.__dict__)
controle = ControleRemoto(tv.volume, tv.canal)
controle.aumentar_volume()
controle.diminuir_volume()
controle.canal()
controle.canal()
controle.canal()
controle.consultar_valor_volume()






