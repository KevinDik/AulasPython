from random import randint
vetor1 = []
vetor2 = []
vetor3 = []
for c in range(1, 11):
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))
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
