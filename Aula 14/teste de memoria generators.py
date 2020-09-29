'''
teste de memoria com generators

for n in fib(10000):
    print(n)
'''

#funcao usando lista 449mb
def fib(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a, b = b, a + b
    return num

# funcao usando geradores


def fib2(max): #3mb
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


#teste
for c in fib2(100000):
    print(c)
