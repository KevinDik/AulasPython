def colore(txt, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(txt) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser um String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {txt} será impresso na cor {cor}')


colore('Geek', 'azul')
