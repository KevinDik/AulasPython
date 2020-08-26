'''def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, TypeError):
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Zero nao divide'


num1 = input('primeiro numero')
num2 = input('segundo numero')
print(dividir(num1, num2))
'''
#comandos pdb
# l listar onde está no codigo
# n proxima linha
# p imprime variavel
# c continua excecução finalizando o debuguging

'''
import pdb
nome = 'angelina'
sobrenome = 'jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em python essencial'
final = nome_completo + 'faz curso' + curso
print(final)
'''

'''
nome = 'angelina'
sobrenome = 'jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em python essencial'
final = nome_completo + 'faz curso' + curso
print(final)
'''

'''
nome = 'angelina'
sobrenome = 'jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em python essencial'
final = nome_completo + 'faz curso' + curso
print(final)
'''

