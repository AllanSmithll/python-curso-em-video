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
Spares = Scoluna3 = MaiorSegLinha = 0

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

        if i != None:  # Soma da terceira coluna, com i diferente de None
            if j == 2:  # Terceira por causa deste if
                Scoluna3 += matriz[i][j]
        else: pass

        if i == 1:
            if j == 0:
                MaiorSegLinha = matriz[i][j]
            elif j == 1 and MaiorSegLinha < matriz[1][j]:
                MaiorSegLinha = matriz[i][j]
            elif j == 2 and MaiorSegLinha < matriz[1][j]:
                MaiorSegLinha = matriz[i][j]
        else:
            continue



    print()
print("-="*30)

print(Spares)
print(Scoluna3)
print(MaiorSegLinha)