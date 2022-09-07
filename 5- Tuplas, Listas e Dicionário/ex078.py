listanum = []
mai = 0
men = 0
for i in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        mai = men = listanum[i]
    else:
        if listanum[i] > mai:
            mai = listanum[i]
        if listanum[i] < men:
            men = listanum[i]
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {mai} nas posições')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}', end='')
print()
print(f'O menor valor digitado foi {men}, nas posições', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}', end='')
print()
