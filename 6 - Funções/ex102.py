# 07/01/2023
'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num:int, show:bool) -> int:
    '''Método que serve para calcular fatorialmente um número inteiro, e solicitar a mostra ou não do processo
    
    Argumentos:

    num: número que será fatorado pela função
    show: ver o processo do cálculo do fatorial
    '''
    if show == True:
        if num != 0:
            cont = 1
            print(f'''
        PROCESSO RECURSIVO DO CÁLCULO FATORIAL\n
        Número n atual ques está sendo fatorado: {num}
        Próximo número que será fatorado: {num-1}
        Explicação: {num} * fatorial({num-1}), onde o programa buscará qual o resultado do fatorial de {num-1}, que será devolvido após o próprio programa achar o resultado de tal cálculo
        ''')
            input("Aperte em ENTER para continuar: ")
        pass
    if num == 0: return 1
    if num >= 1:
        return num * fatorial(num-1, True) # Cálculo do fatorial de forma recursiva


#--------------------#
# PROGRAMA PRINCIPAL #
#--------------------#
while True:
    try:
        numero = int(input("Número para fatorar: "))
    except ValueError:
        print("Digite um número inteiro válido!")
        numero = int(input("Digite um inteiro válido: "))
    ver_calculo_fatorial = input("Ver cálculo fatorial acontecendo (sim ou não)? ").upper().strip()

    if ver_calculo_fatorial == "SIM":
        ver_calculo_fatorial = True
    else:
        ver_calculo_fatorial = False

    print("O fatorial de", numero, "é igual a", fatorial(numero, ver_calculo_fatorial))