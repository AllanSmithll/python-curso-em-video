a = float(input('Digite um número: '))
b = float(input('Digite mais um: '))
c = float(input('Mais outro: '))
#o menor já recebe a letra a.
menor = a
if b < a and c < a:
    menor = b
if c < b and c < a:
    menor = c
#o menor número.
print(f'{menor} é o menor')

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#o maior número
print(f'{maior} é o maior')
print(' ')
print("28/04/2022, maior e menor números.")