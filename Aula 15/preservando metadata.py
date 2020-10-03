'''
metadados sao dados intrisicos em arquivos
wraps sao funcoes que envolvem elementos com diversas finalidades


# problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        """
        Eu sou a funcao (logar) dentro da outra
        :param args:
        :param kwargs:
        :return:
        """
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui esta a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """
    soma dois numeros
    :param a:
    :param b:
    :return:
    """
    return a + b


#print(soma(4, 5))

print(soma.__name__) #nome?
print(soma.__doc__) #documentacao?

problema no metadata pois nçao esta retornando as informações corretas da função
'''

# resolucao
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """
        Eu sou a funcao (logar) dentro da outra
        :param args:
        :param kwargs:
        :return:
        """
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui esta a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """
    soma dois numeros
    :param a:
    :param b:
    :return:
    """
    return a + b


#print(soma(4, 5))

print(soma.__name__) #nome
print(soma.__doc__) #documentacao