total = 0
while True:
    num = int(input('Digite um número inteiro positivo: '))
    if num > 0:
        for c in range(1, num):
            print(c)
            total += num
        break
    print('ERRO!')
print('Total', total)
