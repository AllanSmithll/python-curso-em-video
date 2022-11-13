# 12/11/2022
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Matriz 3X3
lin = 3 # Sendo assim, 3 linhas e 3 colunas
col = 3

for i in range(lin): # Linha começa em 0 e parte para o for j
    for j in range(col): # Após ser inserido os elementos 0 das colunas, volta para o for i, onde será recomeçado em 0 + 1
        matriz[i][j] = int(input(f"Digite um elemento para a posição [{i}, {j}]: ")) # Inserir cada elemento na matriz

print("-="*30)
for i in range(lin):  # Esses for i e for j servem para formatar
    for j in range(col):
        print(f'[{matriz[i][j]:^7}]', end='') # Assim teremos uma matriz que aceita 7 algarismos para estar formatada
    print()   # Esse print serve para pular quando acabar os elementos das linha 0 e as colunas são 0, 1, 2...