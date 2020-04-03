print(f'Números naturais de 1000 divisiveis por 3 e 5')
for c in range(1, 1000):
    if c % 3 == 0 or c % 5 == 0:
        print(f'{c}')
