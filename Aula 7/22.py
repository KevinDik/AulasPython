from random import randint
vetor1 = [randint(1, 100) for valor in range(10)]
vetor2 = [randint(1, 100) for num in range(10)]
vetor3 = []
print('Vetor inicial 1', vetor1)
print('Vetor inicial 2', vetor2)
controle = 0
while controle != 10:
    if controle % 2 == 0:
        vetor3.append(vetor1[controle])
    elif controle % 2 == 1:
        vetor3.append(vetor2[controle])
    controle += 1
print('Vetor final', vetor3)
