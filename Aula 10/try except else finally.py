'''try:
    num = int(input('digite um numero: '))
except ValueError:
    print('numero invalido')
else:
    print('numero digitado ', num)
finally:
    print('sempre será executado')
'''


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, TypeError):
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Zero nao divide'


num1 = input('primeiro numero')
num2 = input('segundo numero')
print(dividir(num1, num2))
'''
Errado
num1 = int(input('primeiro numero'))
try:
    num2 = int(input('segundo numero'))
except ValueError:
    print('Valor devera ser numero')
try:
    print(dividir(num1, num2))
except NameError:
    print('Num errado')
'''

