# 05/01/2023

'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(*numeros):
    '''Método que retorna o maior número de uma tupla qualquer'''
    for n in numeros:
        if numeros is None: return None
        maior = numeros[0]
        n = 1
        while numeros[0+n] > maior:
            maior = numeros[0+n]
            n += 1
        else: continue
    return maior

# Programa principal

maior_numero = maior(10, 12, 30, 100, 200, 250, 1, 3, 0)
print(maior_numero)
