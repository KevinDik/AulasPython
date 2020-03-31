numero = list()
for c in range(1, 11):
    num = int(input(f'Digite o {c}° valor: '))
    numero.append(num)
print(f'O maior valor digitado é {max(numero)}')
print(f'O menor valor digitado é {min(numero)}')
