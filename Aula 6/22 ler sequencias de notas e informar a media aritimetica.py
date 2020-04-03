note = []
media = 0
while True:
    notas = int(input('Digite uma nota: '))
    if 10 <= notas <= 20:
        note.append(notas)
    else:
        print('Encerramento de notas')
        for c in note:
            media += c
        break
print(f'Notas informadas {note}, sua média é de {media/len(note)}')
