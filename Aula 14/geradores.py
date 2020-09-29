'''
generators são iterators
mas nem todo iterator é um generator

generetors podem ser criadors com funcoes geradoras
funcoes geradoras utilizam a palavra yield
generators podem ser criadas com expressoes geradoras

diferenca entre funcoes e generator function

---------------------------------------------------------------
| funcoes               | generator functions                 |
---------------------------------------------------------------
| utiliza return        | ultiliza yield                      |
| retorna um vez        | pode utilizar yiled multiplas vezes |
| exceutada retorna um valor | executada retorna um generator |
---------------------------------------------------------------

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for num in gen:
    print(num)
'''


# funcao geradora

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# uma funcao geradora nao é um generator, mas gera um generator

gen = conta_ate(5) # Se transformado em lista todos serao gerados sem o next


