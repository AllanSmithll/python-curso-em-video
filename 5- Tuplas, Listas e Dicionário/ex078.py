# 11/10/2022
# Exercício para guardar números no array e dizer o maior e o menor números

listanum = []
mai = 0
men = 0
for i in range (0, 5):  # Intervalo para quatro números
    listanum.append(int(input(f'Digite um valor para a posição {i+1}: '))) # Adiciona um elemento à lista "listanum"
    if i == 0:
        mai = men = listanum[i]  # Se i for o primeiro elemento, ele é tanto o maior quanto o menor
    else:
        if listanum[i] > mai:   
            mai = listanum[i]  # Se o elemento for maior que o atual maior da lista, ele torna-se o maior
        if listanum[i] < men:
            men = listanum[i]  # Se o elemento for menor que o atual menor da lista, ele torna-se o menor
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {mai}, na posição', end=' ')
for i, v in enumerate(listanum):  # índice e enumerador
    if v == mai:
        print(f'{i}.', end='')
print()
print(f'O menor valor digitado foi {men}, na posição', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}.', end='')
print()
