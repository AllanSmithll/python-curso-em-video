co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Com os catetos {} e {}, a hipotenusa é {:.2f}.'.format(co, ca, hi))
print('Código feito em 14/01/2022, para encontrar a hipotenusa.')
