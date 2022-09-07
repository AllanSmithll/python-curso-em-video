a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
while cont != 10:
    for i in range(10):
        cont += 1
        if i == 0:
            print(f'{a1} -> ', end='')
        if i > 0:
            print(f'{a1+i*r} -> ', end='')
