cont = 0
cont2 = 0
for i in range(7):
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print(f'Pessoas na maioridade: {cont}.')
print(f'Pessoas menores de 18: {cont2}.')
