def consumo_gas(distancia, gasolina):
    """
    calcula a economia de acordo com os parametros
    :param distancia: quanto o veiculo percorreu
    :param gasolina: combustivel utilizado
    :return: retorna o gasto de combustivel
    """
    consumo = distancia / gasolina
    if consumo < 8:
        print('Venda o carro')
    elif 8 <= consumo <= 14:
        print('Econômico')
    else:
        print('Super econômico')


#Programa principal
distancia = float(input('Informe a distância percorrida: '))
gasolina = float(input('Digite o tanto de conbustivel colocado: '))
consumo_gas(distancia, gasolina)
