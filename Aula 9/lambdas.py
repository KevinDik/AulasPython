def funcao(x):
    return 3 * x + 1

def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

#lambda x: 3 * x + 1


calc = lambda x: 3 * x + 1

print(funcao(7))

print(calc(4))
print(calc(7))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('   keVin', 'DIEGO'))

amar = lambda: 'como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
#n = lambda x1, x1 .... xn: <expressão>
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

autores = ['isac frd', 'ray dgb', 'robert cfrd', 'arthur c fsv', 'frank vdfd', 'auricelia vd v', 'douglas vflx', 'w k vdf', 'kevin vdf']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(3, 0, 1)(2))
