cont = 0
soma = 0
flag = 999
n = 0
while n != flag:
    n = int(input('Digite um número: '))
    if n == flag:
        break
    if n != flag:
        soma += n
        cont += 1
print(f'A soma dos {cont} valores é igual a {soma}.')