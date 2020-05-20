def calculadora(valor1, valor2, sinal):
    """
    Função que permite escolher a operação para dois valores
    :param valor1: primeiro numero
    :param valor2: segundo numero
    :param sinal: sinal da operação
    :return: retorna o valor ja calculado
    """
    if sinal == '+':
        return valor1 + valor2
    elif sinal == '-':
        return valor1 - valor2
    elif sinal == '*':
        return valor1 * valor2
    elif sinal == '/':
        return valor1 / valor2
    else:
        print('Opção inválida')


#Programa principal
print('-'*40)
print('Calculadora simples'.center(40))
print('-'*40)
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite o segundo número: '))
        print('-'*40)
        print('''Digite + para somar
        Digite - para subtrair
        Digite * para multiplicar
        Digite / para dividir 
        ''')
        sinal = str(input('Qual sinal de operação: '))
        print(f'Operação: {num1} {sinal} {num2} = {calculadora(num1, num2, sinal):.2f}')
        break
    except ValueError:
        print('Valor inserido inválido')