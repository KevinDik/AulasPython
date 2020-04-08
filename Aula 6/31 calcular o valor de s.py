# S = 1/1 + 3/2 + 5/4 ... 99/50
par = 1
impar = 0
for c in range(1, 100):
    if c % 2 == 0:
        par += c
    else:
        impar += c
total = impar / par
print(f'A valor de S é igual a {total}')