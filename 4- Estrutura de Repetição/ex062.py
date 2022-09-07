#Melhoramento do exercício 061
print("====GERADOR DE PA====")
print()
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuer mais quantos termos (0 termos significa "não")? '))
print('FIM!')