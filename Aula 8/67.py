def getchar(tecla):
    import keyboard
    while True:
        keyboard.wait(tecla)
        print(f'Tecla pressionada: {tecla}')


# Programa Principal
print('Testando inserção de textos via teclado: ')
getchar(str(input()))


