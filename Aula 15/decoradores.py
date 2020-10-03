'''
decorators sao funções
envolvem outras funções e aprimoram seus comportamentos
tambem sao exemplos de funcoes de maior grandeza Hof
decoratos tem uma sintaxe propria, utilizando @ (syntatic sugar / açucar sintatico)

#decorators como funcoes, sem acucar sintatico


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha uma otimo dia')
    return sendo


def saudacao():
    print('Seja bem vindo a geek university')


#teste 1
teste = seja_educado(saudacao)
print(teste)


#teste 2
def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)
print(raiva_educada)


#Decorator com syntax sugar
def seja_educado_mesmo(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return seja_educado_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é pedro')


#testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()
'''

