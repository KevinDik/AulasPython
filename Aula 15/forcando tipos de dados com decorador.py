'''
forcando tipos de dados com decoradores

'''


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def recebe_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


recebe_msg('geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)