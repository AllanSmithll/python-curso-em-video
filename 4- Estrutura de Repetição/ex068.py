from time import sleep
import random
def iguais(): #Definição da linha de "- e ="
    print("-=-" * 30)

#Jogo do Par ou Ímpar (programa principal)
jogar_novo = 's'
while jogar_novo == 's':
    #Nome do jogador
    jogador = input("Qual o seu nome, jogador? ")
    iguais()
    print('Então, vamos jogar!')
    sleep(2)

    #Jogador escolhe entre par ou impar
    escolha = input('\nImpar ou par? ').lower()
    print(f'Vai aparecer um número de 0 a 10 no resultado. Se {escolha}, você vence. Caso contrário, o computador ganha.')
    sleep(5)
    iguais()
    par_impar = random.randint(0, 10)
    
    #O JOGO EM SI
    if par_impar % 2 == 0:
        num = 'par'
    else:
        num = 'impar'
    
    #Decisão do jogo
    if num == escolha:
        print('PARABÉNS! Você ME VENCEU!')
        print(f'Número {par_impar} é {escolha}.')
    else:
        print('HAHAHA! Mais sorte da próxima vez.')
        print(f'Número {par_impar} não é {escolha}.')
    iguais()
    jogar_novo = input('\nJogar novo jogo (s/n)? ')
    if jogar_novo == 's':
        continue
    else:
        break
print('Paramos por aqui. Obrigado pela jogatina!')
