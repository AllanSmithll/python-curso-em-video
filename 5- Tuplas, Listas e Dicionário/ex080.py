# 18/10/2022
# Cadastrar números numa lista de forma ordenada sem usar sort()

lista = []

for i in range(0, 5):
    num = float(input("Digite um número para a lista: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(lista)