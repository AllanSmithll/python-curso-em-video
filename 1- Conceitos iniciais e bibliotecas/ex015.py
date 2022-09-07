dias = int(input('Quantos dias utilizou o veículo? '))
km = float(input('Quantos quilômetros? '))
Pagamento = (dias * 60) + (km * 0.15)
print('O motorista terá de pagar R${:.2f}.'.format(Pagamento))
