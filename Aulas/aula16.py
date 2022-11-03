#Aula de Tuplas
lanche = 'Sorvete', 'Balas', 'Hambúrguer'
print(lanche[:3])
print(lanche[2])

#Errado, pois tuplas são imutáveis
#lanche[2] = 'Salgado'

#Outras formas de printar na tela

for c in lanche:
    print(f'Vou comer {c}')
print('')

for pos, c in enumerate(lanche):
    print(f'Vou comer {c} da posição {pos}')
print('')

for c in range(0, len(lanche)):
    print(f'Quero comer {lanche[c]}.')

print('DELÍCIA!')
print('')
print(sorted(lanche))

#Concatenação e mais propriedades de tuplas

a = 4, 5, 3
b = 10, 20, 30
c = a + b
print(c)
print(len(c))
print(c.index(30))
print(c.count(4))
del(c)
print('')
print('03/09/2022')
