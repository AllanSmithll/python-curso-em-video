from random import randint
from time import sleep
computador = randint(0, 5) #O computador vai escolher um número
print("=" * 55)
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print("=" * 55)
usu = int(input('Em que número eu pensei? ')) #Usuário tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if computador == usu:
    print("Nãããããooooo!!! Você me venceu.")
else:
    print(f"HAHAHA! Mais sorte da próxima vez! Escolhi o número {computador} e não {usu}.")
#Programa para competir contra o computador
