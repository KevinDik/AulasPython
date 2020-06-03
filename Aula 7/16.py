from random import randint
numeros = [randint(1, 20) for valor in range(5)]
while True:
    try:
        print('''1 - Ver o vetor na orgem direta
2 - Ver o vetor em ordem inversa
0 - sair do programa''')
        opc = int(input('Digite uma das opções: '))
        if opc == 1:
            print(f'Números sorteados {numeros}')
        elif opc == 2:
            print('Ordem inversa do vetor: ', numeros[::-1])
        elif opc == 0:
            print('Finalizando o sistema')
            break
        else:
            print('Desculpe, opção inválida')
    except ValueError:
        print('Erro somente numeros porem ser inseridos')
