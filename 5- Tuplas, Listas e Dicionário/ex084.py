# 12/11/2022
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre quantas pessoas foram cadastradas.

dados = list() # Lista de nomes
pessoas = list() # Lista de pesos
contPessoas = 0 # Quantidade de pessoas
queroMais = 1
mai = men = 0

while queroMais == 1:
    dados.append(input("Nome: "))  # Nome de cada pessoa
    dados.append(float(input("Peso: "))) # Peso de cada pessoa
    pessoas.append(dados[:]) # Adiciono o nome e peso de cada pessoa na lista "pessoas"
    dados.clear() # Depois elimino cada peso e nome que ainda está na lista "dados"
    contPessoas += 1
    mais = input("Mais pessoas(S/N)? ").upper()

    if mais == "S": continue
    elif mais != "N" or mais != "S": break
    else: break

print(pessoas) # Dados de todas as pessoas
print("Foram cadastradas", contPessoas, "pessoas.") # Quantas pessoas foram cadastradas
