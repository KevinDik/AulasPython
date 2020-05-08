from random import randint
vetor = []
controle = 0
while controle != 10:
    valor = randint(1, 15)
    if valor in vetor:
        print('Erro! Numeros não poderão ser repetidos')
    else:
        vetor.append(valor)
        controle += 1
print(f'Valores sorteados sem repetições: {vetor}')