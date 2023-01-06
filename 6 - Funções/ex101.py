# 05/01/2023
'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date
from time import sleep

def voto(ano_nasc:int) -> str:
    '''Método que retorna um valor literal que resulta na analise de aptidão para voto
    
    Argumentos:

    ano_nasc: ano de nascimento da pessoa

    Retorno:

    Valor literal: NEGADO, OBRIGATÓRIO ou OPCIONAL
    '''
    idade = date.today().year - ano_nasc

    print(f'A idade analisada será de {idade} anos. Será que está apto para votar?')
    sleep(2)

    if idade < 0:
        return "IDADE INVÁLIDA"
    if idade < 16 and idade >= 0:
        return "NEGADO"
    elif idade >= 16 and idade <= 17 or idade > 69:
        return "OPCIONAL"
    elif idade >= 18 and idade <= 69:
        return "OBRIGATÓRIO"


#--------------------#
# PROGRAMA PRINCIPAL #
#--------------------#
continua = "S"
while continua == "S" or "SIM" or "SI" or "YES":
    ano_nascimento = int(input("Ano de nascimento: "))
    print(voto(ano_nascimento))
    continua = input("Deseja continuar? ").upper()
    if continua == "S":
        continue
    else:
        break