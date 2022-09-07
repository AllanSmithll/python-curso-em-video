n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
escolha = 0
maior = n1
while escolha != 5:
    print('\nEscolha uma opcão do MENU:')
    print('[1]: Somar')
    print('[2]: Multiplicar')
    print('[3]: Maior')
    print('[4]: Novos Números')
    print('[5]: Sair do programa')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        escolha = n1 + n2
        print(f'{n1} + {n2} = {escolha}')
    elif escolha == 2:
        escolha = n1 * n2
        print(f'{n1} x {n2} = {escolha}')
    elif escolha == 3:
        if n1 > n2:
            escolha = maior
            print(f'O {maior} é maior do que {n2}.')
        if n2 > n1:
            maior = n2
            print(f'O {maior} é maior do que {n1}.')
    elif escolha == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite mais outro: '))
    elif escolha == 5:
        break
    else:
        escolha = input('Número inválido. Digite novamente: ')
print('\nFIM DO PROGRAMA! Até outra hora.')
