vetores = []
for item in range(1, 11):
    vet = (int(input('Digite um valor: ')))
    if vet < 0:
        vetores.append(0)
    else:
        vetores.append(vet)
print(vetores)
