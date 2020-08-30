import


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('Segundo.py esta executando')
else:
    print(f'segundo.py importado {__name__}')