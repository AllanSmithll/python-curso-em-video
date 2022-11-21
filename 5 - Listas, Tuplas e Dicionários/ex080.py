# 18/10/2022
# Cadastrar 5 números numa lista de forma ordenada sem usar sort()

lista = []

for i in range(0, 5):  # 0 a 4
    num = float(input("Digite um número para a lista: "))  # Digitar os números num
    if i == 0 or num > lista[-1]:  # Se num[0], que é o primeiro elemento, ou num é maior que o último elemento da lista
        lista.append(num)  #  Então, coloque-o no final do array
    else:  # Caso não
        pos = 0  # Contador inicial
        while pos < len(lista):    # Faremos uma estrutura de repetição
            if num <= lista[pos]: # Se num for menor ou igual ao elemento na posição "pos" da Lista
                lista.insert(pos, num)  # Insira na posição "pos", o elemento num
                break  # Pare aqui e peça mais um número
            pos += 1   # Incrementa mais um, para que a posição seja escolhida

print(lista)