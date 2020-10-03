'''
Higher order functions

qunado um linguagem de programação suporta HOF indica que podemos ter funções que retorna outras funções como
resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variaveis
 do tipo funcções noo programas

python funções são cidadões de primeira classe, first class citizon

# definindo as funções
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

# nested functions, funções aninnhadas

'''
Em python tbm temos funções dentro de funções que são conhecidas por listed functions ou inner functions, que são
funções internas

#exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'suma daqui', 'gosto muito de você'))
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




