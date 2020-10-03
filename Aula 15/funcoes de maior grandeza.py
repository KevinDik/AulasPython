'''
Higher order functions

qunado um linguagem de programa��o suporta HOF indica que podemos ter fun��es que retorna outras fun��es como
resultado ou mesmo que podemos passar fun��es como argumentos para outras fun��es, e at� mesmo criar variaveis
 do tipo func��es noo programas

python fun��es s�o cidad�es de primeira classe, first class citizon

# definindo as fun��es
def somar(n1, n2):
    return n1 +n2


def diminuir(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def calcular(n1, n2, funcao):
    return funcao(n1, n2)


#testando
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

'''

# nested functions, fun��es aninnhadas

'''
Em python tbm temos fun��es dentro de fun��es que s�o conhecidas por listed functions ou inner functions, que s�o
fun��es internas

#exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'suma daqui', 'gosto muito de voc�'))
    return humor() + pessoa


print(cumprimento('Angelina'))
print(cumprimento('Felicity'))


from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkkk', 'yayayayaya'))
    return rir


rindo = faz_me_rir()
print(rindo())
'''

# inner functions podem acessar o escopo de funcoes externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        r = choice(('hahaha', 'lolololo', 'kkkkkkk'))
        return f'{r} {pessoa}'
    return dando_risada


#teste
rindo = faz_me_rir_novamente('fernanda')
print(rindo())




