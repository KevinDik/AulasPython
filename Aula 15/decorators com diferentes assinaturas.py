'''
decorators com diferentes assinaturas
para resolver o problema abaixo utiliza-se um padrao de projeto chamado
decorator patterns

a assinatura de um funcao em python e representada pelo seu retorno, nome e parametro de entrada

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhada de {acompanhamento}, por favor'


#teste
#print(saudacao('meu zovo'))
print(ordenar('picanha', 'batata'))


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Ola eu so o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Ola eu gostaria de {principal} com {acompanhamento} por favor'


#teste
print(saudacao('felicity'))
print(ordenar('batata', 'sanduiche'))


@gritar
def lol():
    return 'lol'

print(lol())

#obs vale lembrar que podemos utilizar parametros nomeados

print(ordenar(acompanhamento='batata frita', principal='picanha'))
'''

#decorator com argumentos


def verifica_primeiro_arg(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_arg('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_arg(10)
def soma_dez(n1, n2):
    return n1 + n2


#print(soma_dez(20, 10)) # nao permite pois tem que ser 10 o primeiro argumento, nesse caso ele retorna um erro
print(comida_favorita('pizza', 'peixe')) #passa pois foi setado como pizza o primeiro