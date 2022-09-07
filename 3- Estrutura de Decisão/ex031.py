km_via = float(input('Quilômetros percorridos: '))
#Quilômetros viajados
if km_via <= 200:
    valor = km_via * 0.50
    print(f'Você terá de desembolsar R${valor:.2f}')
else:
    valor = km_via * 0.45
    print(f'Você terá de gastar R${valor:.2f}')
print('16/04/2022')
