lista = []
for c in range(1, 11):
    num = int(input(f'Digite o {c}# numero: '))
    lista.append(num)
print(f'A média dos valores listados é de :{sum(lista)/5}')
