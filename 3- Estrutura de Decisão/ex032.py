from datetime import date
ano = int(input('Qual ano será analisado? No caso de 0, o ano atual será analisado: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano BISSEXTO.')
else:
    print(f'{ano} não é um ano BISSEXTO.')
print(' ')
print('Fim! 18/04/2022, para saber se um ano é bissexto')
