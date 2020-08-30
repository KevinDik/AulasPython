'''
modulo sao arquivos com funcoes
pacote sao conjunto de modulos
'''
from geek import geek1, geek2
from geek.university import geek3, geek4
from geek.geek1 import funcao1
from geek.geek2 import funcao2
from geek.university.geek4 import funcao4
from geek.university.geek3 import funcao3

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())