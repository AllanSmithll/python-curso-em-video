Real = float(input('Quantos reais você possui? R$'))
Dólar = Real / 5.65
Euro = Real / 6.41
Iene = Real / 0.050
Yuan = Real / 0.89
print('Se tens R${:.2f}: \nEm dólar: US${:.2f};\nEm euro: E${:.2f};'.format(Real, Dólar, Euro))
print('Em Iene: I${:.2f};\nE em Yuan: Y${:.2f}.'.format(Iene, Yuan))
print('Concluí em 27/12/2021, para ser uma tabela de conversão de moedas.')
