cont = 0 #por quanto vai ser dividido
soma = 0 #soma de idades
while True:
    idade = int(input('Digite uma idade (0 p/interromper o programa): '))
    if idade == 0:
        break
    if idade < 0:
        print('Idade inválida. Digite novamente.')
        continue
    cont += 1
    soma += idade
media = soma / cont
print(f'\nMédia das idades é igual a {media} anos.')
