# 07/01/2023
'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''
# Feito de forma simples

def ficha(nome='<desconhecido>', gols=0) -> str:
    '''
    Este método retorna o desempenho de um jogador, com a quantidade de gols.

    nome: nome do jogador de futebol.
    gols: quantidade de gols do jogador de futebol.
    '''
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

#--------------------#
# PROGRAMA PRINCIPAL #
#--------------------#

nome = str(input("Nome do jogador: "))
gols_feitos = int(input("Gols feitos: "))

ficha(nome, gols_feitos)