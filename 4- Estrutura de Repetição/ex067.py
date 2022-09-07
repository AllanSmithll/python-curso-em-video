n = 0
while n >= 0:
    n = int(input('Digite um número para a tabuada: '))
    if n < 0:
        break
    if n >= 0:
        for i in range(10):
            print(f'{n} * {i + 1 : 2} = {n * (i + 1)}')
print('MISSION COMPLETE!!!')
print("")
print("")
print("Feito em 01/08/2022.")

    