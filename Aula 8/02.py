def dataExt(data):
    """
    Função que recebe uma data em formato xx/xx/xxxx e retorna sua forma extensa
    :param data: valor no formato xx/xx/xxxx
    :return: retorna a data extensa
    """
    mes = data[3:5]
    if mes in '01':
        mesf = 'Janeiro'
    elif mes == '02':
        mesf = 'Fevereiro'
    elif mes == '03':
        mesf = 'Março'
    elif mes == '04':
        mesf = 'Abril'
    elif mes == '05':
        mesf = 'Maio'
    elif mes == '06':
        mesf = 'Junho'
    elif mes == '07':
        mesf = 'Julho'
    elif mes == '08':
        mesf = 'Agosto'
    elif mes == '09':
        mesf = 'Setembro'
    elif mes == '10':
        mesf = 'Outubro'
    elif mes == '11':
        mesf = 'Novembro'
    else:
        mesf = 'Dezembro'

    ano = data[6:]
    print(f'A data digitada é: {data[:2]} de {mesf} de {ano}')


dataExt(str(input('Digite uma data para ver seu extenso xx/xx/xxxx: ')))
