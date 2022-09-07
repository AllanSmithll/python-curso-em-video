larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede possui dimensão {}X{}, e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Será necessário {}l de tinta para pintar essa parede.'.format(tinta))
print('Terminado em 27/12/2021, para saber quantos litros de tinta são necessários para pintar uma parede')
