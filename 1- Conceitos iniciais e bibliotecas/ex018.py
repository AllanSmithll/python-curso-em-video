from math import radians, sin, cos, tan
ângulo = float(input('Valor do ângulo: '))
seno = sin(radians(ângulo))
print('O SENO de {} é igual a {:.2f}.'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O COSSENO de {} é igual a {:.2f}.'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('A TANGENTE de {} é igual a {:.2f}.'.format(ângulo, tangente))
print('Feito em 07/02/2022, para calcular razões trigonométricas.')
