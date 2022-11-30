# 30/11/2022
# Fiz este exercício a um tempo, mas tenho refazê-lo para registrar
'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(larg, compri):
    area = larg * compri
    return area

# Programa principal
l = float(input("Largura do terreno (metros): "))
c = float(input("Comprimento do terreno (metros): "))
print(f"A área de meu terreno é: {area(l, c)}m²")