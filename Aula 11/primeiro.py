def funcao1():
    print('geek university, primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py executando')
else:
    print(f'primeiro.py importado {__name__}')