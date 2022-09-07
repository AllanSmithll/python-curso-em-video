import random
import time

computador = random.randint(1, 10)
jogador = int(input('Advinhe um número entre 1 e 10 que a máquina escolheu: '))
print('\nAguarde...')
time.sleep(2)
while computador != jogador:
    jogador = int(input('\nVocê ERROU! Tente novamente: '))
print(f'\nConseguiu! Você escolheu {jogador} e a máquina também escolheu {computador}.')
