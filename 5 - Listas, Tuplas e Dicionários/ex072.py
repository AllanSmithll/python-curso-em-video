#Tuplas de 0 a 20, por extenso
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

escolha = int(input('Escolha um número de 1 a 20: '))
mais = 'S'

while mais != 'N':
    if escolha == 1:
        print('Você escolheu o número UM.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 2:
        print('Você escolheu o número DOIS.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 3:
        print('Você escolheu o número TRES.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 4:
        print('Você escolheu o número QUATRO.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 5:
        print('Você escolheu o número CINCO.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 6:
        print('Você escolheu o número SEIS.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 7:
        print('Você escolheu o número SETE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 8:
        print('Você escolheu o número OITO.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 9:
        print('Você escolheu o número NOVE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 10:
        print('Você escolheu o número DEZ.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 11:
        print('Você escolheu o número ONZE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 12:
        print('Você escolheu o número DOZE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 13:
        print('Você escolheu o número TREZE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 14:
        print('Você escolheu o número CATORZE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 15:
        print('Você escolheu o número QUINZE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 16:
        print('Você escolheu o número DEZESSEIS.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 17:
        print('Você escolheu o número DEZESSETE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 18:
        print('Você escolheu o número DEZOITO.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 19:
        print('Você escolheu o número DEZENOVE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    if escolha == 20:
        print('Você escolheu o número VINTE.')
        mais = input('Quer mais um número (s/n)? ').upper()
        pass
    elif escolha < 1 and escolha > 20:
        escolha = int(input('ERRADO! Digite entre 1 e 20: '))
        continue
    if mais == 'S':
        escolha = int(input('Escolha outro número: '))
        continue
    elif mais == 'N':
        break

print('Acabou! Última atualização em 08/09/2022')
    
