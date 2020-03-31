while True:
    numero = int(input('Digite um número entre 100 a 999: '))
    if numero >= 100:
        num = str(numero)
        print(f"""Centena: {num[0]}
Dezena: {num[1]}
Unidade: {num[2]}
        """)
        break
    print('\033[31mErro! Digite um número entre os parametros\033[m')
