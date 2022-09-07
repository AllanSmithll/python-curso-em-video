flag = 999
c = n = s = 0
while n != flag:
    n = int(input('Digite um número: '))
    if n == flag:
        break
    if n != flag:
        s += n
        c += 1
print(f'A soma dos {c} valores é igual a {s}.')
