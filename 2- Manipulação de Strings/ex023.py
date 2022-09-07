num = int(input('Digite um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando:')
print('A unidade é o {}'.format(uni))
print('A dezena é o {}'.format(dez))
print('A centena é o {}'.format(cen))
print('A milhar é o {}'.format(mil))
print(' ')
print('Feito em 24/02/2022')
