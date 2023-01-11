# 11/01/2023
# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(valor, aumento):
    '''Método que aumenta um valor pela pocentagem.
    
    Argumentos:

    valor: valor a ser aumentado
    aumento: porcentagem que será aumentada sobre o valor.
    '''
    return valor + (valor * aumento / 100)

def diminuir(valor, diminuicao):
    '''Método que diminui um valor pela pocentagem.
    
    Argumentos:

    valor: valor a ser diminuído
    diminuicao: porcentagem que será diminuído o valor.
    '''
    return valor - (valor * diminuicao / 100)

def dobro(valor):
    '''Dobro de um valor digitado.
    
    Argumentos:
    
    valor: valor a ser dobrado.
    '''
    return valor * 2

def metade(valor):
    '''Metade de um valor digitado.
    
    Argumentos:
    
    valor: valor a ser dividido pela metade.
    '''
    return valor / 2