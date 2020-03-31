num = int(input('Digite quantos números serão lidos: '))
lista = []
maiores = []
for c in range(1, num+1):
    valor = int(input(f'Informe o {c} número: '))
    lista.append(valor)
for item in lista:
    if item == max(lista):
        maiores.append(item)
print('lista de números informados', lista)
print(f'O maior valor informado é de {maiores[0]}, aparececimento: {len(maiores)} ')
