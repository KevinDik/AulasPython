# S = 0 + 1 / 2! + 2 / 4!...
valor = int(input('Digite um número: '))
fatorial = []
num = 0
for item in range(1, valor+1):
    fatorial.append(item)
for item in fatorial:
    if item % 2 == 0:
        num = num + 1 / item
print(f'Para a formula S = 0 + 1 / 2!... De acordo com o valor informado {valor} o resultado é de {num}')