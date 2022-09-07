frase = input('Forme uma frase (sem acentos): ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inversao = junto[::-1]
print(f'Sua frase {junto} ao contrário é {inversao}.')
if inversao == junto:
    print('Então é um palíndromo.')
else:
    print('Então não é um palíndromo.')