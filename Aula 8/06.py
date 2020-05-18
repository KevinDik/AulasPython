def converhoras(hora, minuto, segundo):
    hora = hora * 3600
    minuto = minuto * 3600
    total = hora + minuto + segundo
    print(hora, minuto, segundo)
    return print(f'Conforme informado:\nTotal de Segundos {total}')


# Programa principal
hora = int(input('Digite a hora: '))
min = int(input('Minutos: '))
seg = int(input('Segundos: '))
converhoras(hora, min, seg)
