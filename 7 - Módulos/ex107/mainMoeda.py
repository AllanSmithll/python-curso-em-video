# 11/01/2023, main do moeda.py
from moeda import *

valor = float(input("Digite um valor: R$"))
aumento = float(input("Quanto deseja aumentar (%)? "))
diminuicao = float(input("Quanto deseja diminuir (%)? "))

print(f"O valor aumentado fica assim: R${aumentar(valor, aumento)}")

print(f"O valor diminuido fica assim: R${diminuir(valor, diminuicao)}.")

print(f"O dobro do valor é R${dobro(valor)}.")

print(f"A metade do valor é R${metade(valor)}.")