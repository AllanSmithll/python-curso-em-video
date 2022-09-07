km_h = int(input('Velocidade do carro (Km/h): '))
limite = 80
multa = (km_h - limite) * 7

if km_h > limite:
    print('Você vai pagar R${:.2f} de multa.'.format(multa))
else:
    print('Fique tranquilo! Você não será multado.')
#Sobre multa. Achei meio difícil, mas consegui fazer sem ajuda. 07/04/2022.
