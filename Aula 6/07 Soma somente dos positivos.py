soma = 0
for c in range(1, 11):
    num = int(input(f'Digite o {c}º numero: '))
    if num % 2 == 0:
       soma += num
print(f'A soma dos valores pares digitados foi de {soma}')
