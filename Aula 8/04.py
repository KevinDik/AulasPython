def quadrper(numero):
    if numero ** numero == numero ** 2:
        print(f'O numero {numero} é um quadrado perfeito, pois a multiplicação de {numero} x {numero} é de {numero**2}')
    print(f'O número {numero} não é um quadrado perfeito')


quadrper(int(input('Digite um número: ')))