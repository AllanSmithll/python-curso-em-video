# 03/11/2022
# Estrutura composta (a lista) em que um conjunto de listas está dentro de outra lista principal


""" Caso 1: criaremos uma lista "teste", onde será adicionado vários elementos nela. Logo após a inserção de cada dado (nome e idade atual), será colocado dentro de outra lista(galera). """

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Allan"
teste[1] = 17
galera.append(teste[:])
teste[0] = "Anderson"
teste[1] = 18
# print(teste) Só leva em consideração os últimos elementos que foram declarados ['Anderson', 18]
galera.append(teste[:])
print(teste)