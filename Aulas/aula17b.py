# 03/11/2022
# Estrutura composta (a lista) em que um conjunto de listas está dentro de outra lista principal


""" Caso 1: criaremos uma lista "pessoa", onde será adicionado vários elementos nela. Logo após a inserção dos dados (nome e idade atual), será colocado dentro de outra lista(galera). """

pessoa = list()
pessoa.append('Gustavo')
pessoa.append(40)
galera = list()
galera.append(pessoa[:])
pessoa[0] = "Allan"
pessoa[1] = 17
galera.append(pessoa[:])
pessoa[0] = "Anderson"
pessoa[1] = 18
# print(pessoa) Só leva em consideração os últimos elementos que foram declarados ['Anderson', 18]
galera.append(pessoa[:])
print(galera)

''' Caso 2: vou pegar essa lista "galera" que fiz anterior, e vou manipulá-la'''

print(galera[0][0])
print(galera[1] [0])
print(galera[2][1])

for p in galera:
    print(f"\n{p[0]} tem {p[1]} anos de idade.\n")


''' Caso 3: vou agora pegar o nome e a idade a partir do teclado'''

galera2 = list()
dados = list()
for i in range(0, 3):
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    galera2.append(dados[:])
    dados.clear()

print(galera2)