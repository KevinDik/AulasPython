from time import sleep
num = 10
while True:
    print(num)
    num -= 1
    sleep(1)
    if num == 0:
        break
print('Fim')
