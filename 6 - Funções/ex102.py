# 05/01/2023
'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num:int) -> int:
    '''Método que serve para calcular fatorialmente um número inteiro
    
    Argumentos:

    num: número que será fatorado pela função
    '''
    pass


#--------------------#
# PROGRAMA PRINCIPAL #
#--------------------#
numero = int(input("Número para fatorar: "))
print("O fatorial de", numero, "é", fatorial(numero))