# 16/11/2022
# Exercício 086 melhorado, agora com os seguintes requisitos:
'''
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior maior da segunda coluna
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Matriz 3X3
lin = 3
col = 3
Spares = Scolunas = MaiorSegLinha = 0

for i in range(lin):
    for j in range(col):
        matriz[i][j] = int(input(f"Digite um elemento para a posição [{i}, {j}]: ")) 

print("-="*30)
for i in range(lin):
    for j in range(col):
        print(f'[{matriz[i][j]:^7}]', end='')
        
        if matriz[i][j] % 2 == 0:  # Soma de todos os valores pares digitados
            Spares += matriz[i][j]
        else: pass

        if matriz[i][2]:
            Scolunas += matriz[i][2]
        else: continue


    print()

print(Spares)
print(Scolunas)