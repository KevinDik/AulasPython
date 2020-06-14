def doubleFact(num):
    unidade = 0
    total = 0
    while True:
        unidade = num - 1
        total = num * unidade
        print(total)
        if num == 1:
            break


# Programa Pricipal
while True:
    try:
        num = int(input('Digite um número ímpar: '))
        if num % 2 == 1:
            doubleFact(num)
            break
        print('\033[31mNúmero digitado não é impar\033[m')
    except ValueError:
        print('\033[31mValor digitado não é um número impar\033[m')