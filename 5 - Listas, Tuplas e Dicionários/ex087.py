# 16/11/2022
# Exercício 086 melhorado, agora com os seguintes requisitos:
'''
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior maior da segunda coluna
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Matriz 3X3
lin = 3  # Número de Linhas
col = 3  # Número de colunas
Spares = Scoluna3 = MaiorSegLinha = 0
# Soma de pares = Soma de Colunas = Maior da Segunda Linhas = 0

for i in range(lin):
    for j in range(col):
        matriz[i][j] = int(input(f"Digite um elemento para a posição [{i}, {j}]: ")) # Mudando os 0s por números ditos pelo usuário

print("-="*30)
for i in range(lin):
    for j in range(col):
        print(f'[{matriz[i][j]:^7}]', end='') # Formatação da matriz
        
        if matriz[i][j] % 2 == 0:  
            Spares += matriz[i][j] # Soma de todos os valores pares digitados
        else: pass

        if i != None:
            if j == 2:  # Terceira linha por causa deste if
                Scoluna3 += matriz[i][j] # Soma da terceira coluna, com i diferente de None
        else: pass

        if i == 1: # Só vale para a segunda linha
            if j == 0:
                MaiorSegLinha = matriz[i][j] # Linha 1, primeira coluna, com certeza será o maior no começo
            elif j == 1 and MaiorSegLinha < matriz[1][j]:
                MaiorSegLinha = matriz[i][j] # Se o linha 1, segunda coluna maior do que o coluna 1, ele será o maior da linha 1
            elif j == 2 and MaiorSegLinha < matriz[1][j]:
                MaiorSegLinha = matriz[i][j] # Se o linha 1, terceira coluna maior do que o maior atual, será o maior da linha 1.
        else:
            continue



    print()
print("-="*30)

print(Spares)
print(Scoluna3)
print(MaiorSegLinha)